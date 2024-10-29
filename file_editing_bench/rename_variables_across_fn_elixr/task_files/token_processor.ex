defmodule Auth.TokenProcessor do
  @moduledoc """
  Handles processing and validation of authentication tokens.
  """

  def process_token(tkn) do
    with {:ok, decoded} <- decode_token(tkn),
         {:ok, validated} <- validate_token(decoded),
         {:ok, enriched} <- enrich_token_data(validated) do
      {:ok, enriched}
    else
      {:error, reason} -> {:error, reason}
    end
  end

  defp decode_token(tkn) do
    case Base.decode64(tkn) do
      {:ok, decoded} -> {:ok, decoded}
      :error -> {:error, :invalid_encoding}
    end
  end

  defp validate_token(tkn) do
    cond do
      String.length(tkn) < 32 ->
        {:error, :token_too_short}
      not String.printable?(tkn) ->
        {:error, :invalid_characters}
      true ->
        {:ok, tkn}
    end
  end

  defp enrich_token_data(tkn) do
    metadata = %{
      length: String.length(tkn),
      checksum: :crypto.hash(:sha256, tkn) |> Base.encode16(),
      timestamp: DateTime.utc_now()
    }
    
    {:ok, Map.put(metadata, :original_token, tkn)}
  end
end