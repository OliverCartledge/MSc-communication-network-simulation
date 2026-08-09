from csvEditor import (
    createVisualCSV,
    set_Framing,
    addToVisualCSV
)

set_Framing("left", 1, "random", "text")

createVisualCSV()

addToVisualCSV(
    current_agent_id=1,
    transferred_from_agent_id=0,
    role="positive",
    original_message="Gun violence in Chicago is increasing.",
    recieved_message="Gun violence in Chicago has increased, particularly among young people.",
    generated_image_path="test_images/agent1.png",
    generated_image_description="An urban Chicago street with police responding to a shooting.",
    similarity_to_previous=0.82,
    global_similarity_to_original=0.76,
    sentiment_analysis="negative",
    depth=1
)

addToVisualCSV(
    current_agent_id=2,
    transferred_from_agent_id=1,
    role="negative",
    original_message="Gun violence in Chicago is increasing.",
    recieved_message="Gun violence in Chicago has increased, particularly among young people.",
    generated_image_path="test_images/agent2.png",
    generated_image_description="A disturbing urban scene showing police responding to violent activity.",
    similarity_to_previous=0.79,
    global_similarity_to_original=0.71,
    sentiment_analysis="negative",
    depth=2
)

print("Visual CSV test complete.")