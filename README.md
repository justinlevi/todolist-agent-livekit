# running this locally

```
conda activate livekit
pip install -r ./requirements.txt
 python app.py dev
```

# openweb ui

- http://host.docker.internal:8000/v1
- your-secret-api-\*\*\*

# env requirements

OPENAI_API_KEY=xxx
BACKEND_API_KEY=xxx
BACKEND_API_URL=https://xxx.fly.dev/v1
INITIAL_GREETING="XXX"

## Livekit settings

- https://cloud.livekit.io/projects/p_67qw2anl5xa/settings/keys

## Livekit playground

- https://agents-playground.livekit.io/
- currently using test cloud env

## Livekit Agents Docs

- https://github.com/livekit/agents
  https://docs.livekit.io/agents/voice-agent/voice-pipeline/

## Fly io Dev

- https://fly.io/apps/livekit-ai-answering-service
