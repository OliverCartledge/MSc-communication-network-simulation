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
    3: {
        "name": "Annual arrests at southern border top 2 million for first time",
        "left": "Annual U.S. border arrivals top 2 million, fueled by record migration from Venezuela, Cuba and Nicaragua",
        "centre": "More than 2 million were arrested at the southern border, a record",
        "right": "Border Arrests Top 2 Million for First Time Ever"
    },
    4: {
        "name": "Amy Coney Barrett confirmed to the supreme court",
        "left": "Amy Coney Barrett has officially been confirmed as a Supreme Court justice",
        "centre": "GOP Senate confirms Trump Supreme Court pick to succeed Ginsburg",
        "right": "Senate confirms Amy Coney Barrett to Supreme Court, cements 6-3 conservative majority"
    },
    5: {
        "name": "2022 Elections: Dems keep senate, and more results of competitive races",
        "left": "Democrats keep Senate majority as GOP push falters in Nevada",
        "centre": "Democrats Keep Control of Senate as Red Wave Fails to Materialize",
        "right": "Republican Party 'is dead' after major midterm election losses in Arizona, Pennsylvania, Nevada: Hawley"
    },
    6: {
         "name": "AG Garland launches probe into Minneapolis police department",
         "left": "Attorney General Merrick Garland announces an investigation into the Minneapolis Police Department.",
         "centre": "George Floyd murder: Minneapolis police to face US federal probe",
         "right": "AG Garland Opens Probe into Unconstitutional Practices at Minneapolis Police Department"
    },
    7: {
         "name": "Amazon raises minimum wage to $15 an hour",
         "left": "Amazon boosts minimum wage to $15 for all workers following criticism",
         "centre": "Amazon to Raise Its Minimum U.S. Wage to $15 an Hour",
         "right": "Amazon hikes minimum wage to $15 for all US employees"
    },
    8: {
         "name": "Antiviral Drug Remdesivir approved as COVID-19 treatment by FDA",
         "left": "FDA approves remdesivir as treatment for COVID-19 patients in hospital",
         "centre": "FDA Approves Remdesivir for Hospitalized COVID-19 Patients After Drug Was Used to Treat Trump",
         "right": "FDA approves antiviral drug remdesivir as coronavirus treatment"
    },
    9: {
         "name": "200 Days After Invading, Russians Losing Ground Against Ukrainian Offensive",
         "left": "Ukraine pushes big counteroffensive as war marks 200 days",
         "centre": "Kharkiv offensive: Ukrainian army says it has tripled retaken area",
         "right": "Taken By Surprise: Russian Forces Retreat Under Major Ukrainian Counteroffensive On Eastern Front"
    },
    10: {
         "name": "Amazon Offers Vaccine Distribution Aid to Biden Administration",
         "left": "Amazon to Biden: Prioritize our workers for the vaccine",
         "centre": "Amazon offers to help Biden administration with COVID vaccine efforts",
         "right": "Why did Amazon wait until Bidens inauguration to offer help with vaccine distribution?"
    },
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
