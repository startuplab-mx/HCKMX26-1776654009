root_agent = Agent(
    name="safety_guardian",
    model=Gemini(
        model="gemini-2.5-flash-lite",
        retry_options=retry_config
    ),
    description="A simple agent that protect children from narco recruitment and dangerouse online content.",
    instruction="You are the Digital Guardian AI," \
    " a specialized safety specialist focused on " \
    "protecting minors (under 18) from " \
    "online exploitation, specifically targeting " \
    "recruitment efforts by organized crime (cartels)"
    " and exposure to extreme "narcocultura" or "
    "violent content.",
    tools=[google_search],
)

print("✅ Root Agent defined.")