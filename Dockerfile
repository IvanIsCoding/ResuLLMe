FROM ghcr.io/prefix-dev/pixi:0.47.0-noble

COPY . /app

WORKDIR /app

RUN rm -rf /app/.pixi

RUN pixi install -e default

ENV GEMINI_API_KEY=''

ENV OPENAI_API_KEY=''

EXPOSE 8502

CMD ["pixi", "run", "run-app"]
