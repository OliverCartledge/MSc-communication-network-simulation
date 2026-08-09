STORIES = {
    1: {
        "name": "Gun violence over fourth of July weekend",
        "left": "Chicago Gun Violence Spikes and Increasingly Finds the Youngest Victims",
        "centre": "Bullets just came from nowhere: Fourth of July weekend gun violence kills at least 17, including 7-year-old-girl",
        "right": "Dozens of shootings across US mark bloody July 4th weekend"
    },
    2: {
        "name": "Abbott baby formula plant halts production again",
        "left": "Formula production at Abbott's Michigan plant delayed after flooding from severe storms",
        "centre": "Abbott Nutrition again pauses baby formula production in Sturgis",
        "right": "Abbott baby formula plant floods in Michigan, halting production for 'weeks'"
    },

    # TODO: add the remaining stories
}

def get_story(story_id, framing):
    story = STORIES.get(story_id)

    if story is None:
        raise KeyError(f"Unknown story_id: {story_id}")

    if framing not in story:
        raise KeyError(f"Unknown framing '{framing}' for story {story_id}")

    return {
        "story_id": story_id,
        "name": story["name"],
        "framing": framing,
        "headline": story[framing]
    }
