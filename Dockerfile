FROM python:3.8.2

LABEL version="1.0"

LABEL maintainer="andrzej.drzystek@gmail.com"

ENV VIRTUAL_ENV /venv

ENV PATH $VIRTUAL_ENV/bin:$PATH

RUN apt-get update \
    && apt-get --yes autoremove --purge \
    && apt-get clean \
    && rm -rf /tmp/* \
    && rm -rf /var/lib/apt/lists/*

RUN python -m venv /venv

COPY requirements.txt ./

RUN pip install \
    --no-cache-dir \
    --disable-pip-version-check \
    --requirement requirements.txt

COPY . .

ENTRYPOINT ["python", "./main.py"]

CMD ["--help"]
