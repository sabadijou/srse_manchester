
FROM python:3.10-slim

WORKDIR /usr/src/srse_manchester

RUN python -m venv /usr/src/srse_manchester/venv

ENV PATH="/usr/src/srse_manchester/venv/bin:$PATH"

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 80

ENV NAME SRSE_MANCHESTER

CMD ["python", "./explorer.py"]
