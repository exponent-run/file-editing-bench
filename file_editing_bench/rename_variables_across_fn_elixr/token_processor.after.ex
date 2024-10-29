defmodule Auth.TokenProcessor do
  @moduledoc """
  Handles processing and validation of authentication tokens.
  """

  def process_token(token) do
    with {:ok, decoded} <- decode_token(token),
         {:ok, validated} <- validate_token(decoded),
         {:ok, enriched} <- enrich_token_data(validated) do
      {:ok, enriched}
    else
      {:error, reason} -> {:error, reason}
    end
  end

  defp decode_token(token) do
    case Base.decode64(token) do
      {:ok, decoded} -> {:ok, decoded}
      :error -> {:error, :invalid_encoding}
    end
  end

  defp validate_token(token) do
    cond do
      String.length(token) < 32 ->
        {:error, :token_too_short}
      not String.printable?(token) ->
        {:error, :invalid_characters}
      true ->
        {:ok, token}
    end
  end

  defp enrich_token_data(token) do
    metadata = %{
      length: String.length(token),
      checksum: :crypto.hash(:sha256, token) |> Base.encode16(),
      timestamp: DateTime.utc_now()
    }
    
    {:ok, Map.put(metadata, :original_token, token)}
  end
end