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
         #"left": "Amazon.com announced Tuesday that it will raise its minimum wage to $15 an hour for all employees, a move that comes after the tech giant faced harsh criticism for how much it pays its workers.",
         "centre": "Amazon to Raise Its Minimum U.S. Wage to $15 an Hour",
         #"centre": "Amazon.com Inc. on Tuesday said it was raising the minimum wage it pays all U.S. workers to $15 an hour, a move that comes as the company faced increased criticism about pay and benefits for its warehouse workers.",
         "right": "Amazon hikes minimum wage to $15 for all US employees"
         #"right": "All U.S. Amazon employees, full-time, part-time, temporary and seasonal, will earn $15 per hour, effective Nov. 1. According to a press release from the company, the new minimum wage will benefit more than 250,000 Amazon employees as well as over 100,000 seasonal employees that will be hired at Amazon across the country this holiday season.",
    },
    8: {
         "name": "Antiviral Drug Remdesivir approved as COVID-19 treatment by FDA",
         "left": "FDA approves remdesivir as treatment for COVID-19 patients in hospital",
         #"left": "The Food and Drug Administration (FDA) on Thursday approved the antiviral drug remdesivir as a treatment for patients with COVID-19 who require hospitalization.Given through an IV, remdesivir works to stop replication of SARS-CoV-2, the virus that causes COVID-19, according to the drug's manufacturer, California-based Gilead Sciences, Inc. Previously authorized by the FDA for emergency use to treat COVID-19, the drug is now the first and only approved COVID-19 treatment in the United States, Gilead said in a release.",
         "centre": "FDA Approves Remdesivir for Hospitalized COVID-19 Patients After Drug Was Used to Treat Trump",
         #"centre": "The Food and Drug Administration (FDA) on Thursday approved remdesivir for the treatment of hospitalized COVID-19 patients. The antiviral treatment, which is made by Gilead Sciences and sold as Veklury, was used to treat President Donald Trump after he contracted the virus earlier this month. Remdesivir previously received emergency use authorization from the FDA in May for patients with severe cases of COVID-19. The agency later expanded its emergency use authorization in August to include patients who were hospitalized as a result of their COVID-19 infections.",
         "right": "FDA approves antiviral drug remdesivir as coronavirus treatment"
         #"right": "The Food and Drug Administration granted approval of remdesivir, an antiviral drug from Gilead Sciences and a treatment for COVID-19. The drug, sold under the name Veklury, will be used for hospitalized COVID-19 patients, Gilead said. It is the first coronavirus disease treatment to receive FDA approval. The approval of Veklury marks an important milestone in efforts to help address the pandemic by offering an effective treatment that helps patients recover faster and, in turn, helps preserve scarce healthcare resources.",
    },
    9: {
         "name": "200 Days After Invading, Russians Losing Ground Against Ukrainian Offensive",
         "left": "Ukraine pushes big counteroffensive as war marks 200 days",
         #"left": "As the war in Ukraine marked 200 days on Sunday, the country has reclaimed broad swaths of the south and east in a long-anticipated counteroffensive that has dealt a heavy blow to Russia.The counterattack began in the final days of August and at first focused on the southern region of Kherson, which was swept by Russian forces in the opening days of the invasion. But just as Moscow redirected attention and troops there, Ukraine launched another, highly effective offensive in the northeast, near Kharkiv.",
         "centre": "Kharkiv offensive: Ukrainian army says it has tripled retaken area",
         #"centre": "Ukraine's military says its forces have retaken over 3,000 sq km (1,158 sq miles) during a rapid counter-offensive in eastern Ukraine. The remarkable advance, if confirmed, means Kyiv's forces have tripled their stated gains in little over 48 hours.On Thursday evening, President Zelensky put the figure at 1,000 sq km, and then 2,000 sq km on Saturday evening. The BBC cannot verify the Ukrainian figures, and journalists have been denied access to the frontlines.",
         "right": "Taken By Surprise: Russian Forces Retreat Under Major Ukrainian Counteroffensive On Eastern Front"
         #"right": "Moscow abandoned two major areas in Ukraine Kharkiv region Saturday after Ukrainian forces choked out a major supply point for Russian troops. In order to achieve the declared goals of the special military operation for the liberation of Donbas, it was decided to regroup the Russian forces stationed near Balakleya and Izyum to boost efforts in the Donetsk direction, Russian Defense Ministry Spokesman Igor Konashenkov told TASS.",
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
