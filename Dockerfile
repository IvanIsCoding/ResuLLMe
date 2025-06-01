FROM ghcr.io/prefix-dev/pixi:0.47.0-noble

# copy source code, pixi.toml and pixi.lock to the container
COPY . /app
WORKDIR /app
RUN rm -rf /app/.pixi
RUN pixi install -e default

ENV GEMINI_API_KEY=''
ENV OPENAI_API_KEY=''
EXPOSE 8501

CMD ["pixi", "run", "run-app"]
