defmodule Auth.TokenProcessor do
  @moduledoc """
  Handles processing and validation of authentication tokens.
  """

  def process_token(tkn) do
    with {:ok, dec} <- decode_token(tkn),
         {:ok, val} <- validate_token(dec) do
      {:ok, extract_claims(val)}
    else
      {:error, reason} -> {:error, reason}
    end
  end

  defp decode_token(tkn) do
    case Base.decode64(tkn) do
      {:ok, dec} -> {:ok, dec}
      :error -> {:error, :invalid_encoding}
    end
  end

  defp validate_token(dec) do
    case String.split(dec, ".", parts: 3) do
      [_h, p, _s] = val when byte_size(p) > 0 -> {:ok, val}
      _ -> {:error, :invalid_format}
    end
  end

  defp extract_claims([_h, p, _s]) do
    p
    |> Base.decode64!()
    |> Jason.decode!()
  end
end