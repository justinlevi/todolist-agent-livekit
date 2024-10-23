import logging
import os

from dotenv import load_dotenv
from livekit.agents import AutoSubscribe, JobContext, WorkerOptions, cli, llm
from livekit.agents.pipeline import VoicePipelineAgent
from livekit.plugins import deepgram, openai, silero

load_dotenv()
logger = logging.getLogger("openai_assistant")

api_key = os.getenv("BACKEND_API_KEY")
api_url = os.getenv("BACKEND_API_URL")

initial_greeting = os.getenv("INITIAL_GREETING")

llm = openai.LLM(base_url=api_url, api_key=api_key)


async def entrypoint(ctx: JobContext):

    await ctx.connect(auto_subscribe=AutoSubscribe.AUDIO_ONLY)
    await ctx.wait_for_participant()

    assistant = VoicePipelineAgent(
        vad=silero.VAD.load(activation_threshold=0.65),
        stt=deepgram.STT(),
        tts=openai.TTS(),
        llm=llm,
        # whether the agent can be interrupted
        allow_interruptions=True,
        # sensitivity of when to interrupt
        interrupt_speech_duration=0.6,
        interrupt_min_words=0,
        # minimal silence duration to consider end of turn
        min_endpointing_delay=0.5,
    )
    assistant.start(ctx.room)

    await assistant.say(initial_greeting, allow_interruptions=False)


if __name__ == "__main__":
    cli.run_app(WorkerOptions(entrypoint_fnc=entrypoint))
