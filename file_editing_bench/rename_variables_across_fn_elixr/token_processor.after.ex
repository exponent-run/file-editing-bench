defmodule Auth.TokenProcessor do
  @moduledoc """
  Handles processing and validation of authentication tokens.
  """

  def process_token(token) do
    with {:ok, decoded_token} <- decode_token(token),
         {:ok, token_parts} <- validate_token(decoded_token) do
      {:ok, extract_claims(token_parts)}
    else
      {:error, reason} -> {:error, reason}
    end
  end

  defp decode_token(token) do
    case Base.decode64(token) do
      {:ok, decoded_token} -> {:ok, decoded_token}
      :error -> {:error, :invalid_encoding}
    end
  end

  defp validate_token(decoded_token) do
    case String.split(decoded_token, ".", parts: 3) do
      [_h, payload, _s] = token_parts when byte_size(payload) > 0 -> {:ok, token_parts}
      _ -> {:error, :invalid_format}
    end
  end

  defp extract_claims([_h, payload, _s]) do
    payload
    |> Base.decode64!()
    |> Jason.decode!()
  end
end