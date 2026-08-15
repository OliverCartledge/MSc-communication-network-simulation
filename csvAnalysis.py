import pandas as pd

qwen = pd.read_csv("csvFolder/textualCSV.csv")
llama = pd.read_csv("csvFolder/textualCSVLlama.csv")

visual = pd.read_csv("csvFolder/visualCSV.csv")

llama_article = pd.read_csv("csvFolder/article_textualCSV.csv")
visual_article = pd.read_csv("csvFolder/article_visualCSV.csv")

##checks to make sure the CSVs were added correctly
##print("qwen rows: " , len(qwen))
##print("llama rows: " , len(llama))
##
##print("\nqwen cols: ")
##print(qwen.columns.tolist())
##
##print("\nllama cols: ")
##print(llama.columns.tolist())
#
##print prop depths for each model type
#print("\nQwen propagation depths: ")
#print(qwen["Propagation Depth"].value_counts().sort_index())
#
#print("\nLlama propagation depths: ")
#print(llama["Propagation Depth"].value_counts().sort_index())

#global similarity by propagation depth
#global_qwen = (qwen.groupby("Propagation Depth")["Global Similarity To Original"].agg(["count", "mean", "median", "std"]).reset_index())
#global_llama = (llama.groupby("Propagation Depth")["Global Similarity To Original"].agg(["count", "mean", "median", "std"]).reset_index())

#print("\nQwen global similarity:")
#print(global_qwen)

#print("\nLlama global similarity:")
#print(global_llama)

#print("\nOverall global similarity")
#
#print("Qwen:")
#print(qwen["Global Similarity To Original"].describe())
#
#print("Llama:")
#print(llama["Global Similarity To Original"].describe())

##local similarity by propagation depth
#local_qwen = (qwen.groupby("Propagation Depth")["Similarity To Previous"].agg(["count", "mean", "median", "std"]).reset_index())
#local_llama = (llama.groupby("Propagation Depth")["Similarity To Previous"].agg(["count", "mean", "median", "std"]).reset_index())
#
#print("\nQwen local similarity:")
#print(local_qwen)
#
#print("\nLlama local similarity:")
#print(local_llama)
#
#
#print("\nOverall local similarity")
#
#print("Qwen:")
#print(qwen["Similarity To Previous"].describe())
#
#print("Llama:")
#print(llama["Similarity To Previous"].describe())
#
#global_qwen.to_csv("global_Qwen_Similarity_Summary.csv", index = False)
#global_llama.to_csv("global_Llama_Similarity_Summary.csv", index = False)
#
#local_qwen.to_csv("local_Qwen_Similarity_Summary.csv", index = False)
#local_llama.to_csv("local_Llama_Similarity_Summary.csv", index = False)

#global similarity by story and propagation depth 
#qwen_story_by_propagation = (qwen.groupby(["Story ID", "Propagation Depth"])["Global Similarity To Original"].agg(["count", "mean", "median", "std"]).reset_index())
#llama_story_by_propagation = (llama.groupby(["Story ID", "Propagation Depth"])["Global Similarity To Original"].agg(["count", "mean", "median", "std"]).reset_index())

#qwen_story_overall = (qwen.groupby(["Story ID"])["Global Similarity To Original"].agg(["count", "mean", "median", "std"]).reset_index())
#llama_story_overall = (llama.groupby(["Story ID"])["Global Similarity To Original"].agg(["count", "mean", "median", "std"]).reset_index())

#print("\nQwen:")
#print(qwen_story_by_propagation.to_string(index=False))
#print("\nOverall:")
#print(qwen_story_overall.to_string(index=False))

#print("\nLlama:")
#print(llama_story_by_propagation.to_string(index=False))
#print("\nOverall:")
#print(llama_story_overall.to_string(index=False))
#
#story_comparions = qwen_story_overall[
#    ["Story ID", "mean"]
#].rename(columns={"mean": "Qwen Mean"})
#
#story_comparions = story_comparions.merge(
#    llama_story_overall[["Story ID", "mean"]].rename(
#        columns={"mean": "Llama Mean"}
#    ),
#    on="Story ID"
#)
#
#story_comparions["Differences"] = (
#    story_comparions["Llama Mean"]
#    - story_comparions["Qwen Mean"]
#)
#
#
#print("\nQwen vs Llama sematnic evolution by story:")
#print(story_comparions.to_string(index=False))
#story_comparions.to_csv("global_QwenVLlama_by_story.csv", index=False)

#qwen_neutral = qwen[qwen["Role selection"] == "neutral"]
#llama_neutral = llama[llama["Role selection"] == "neutral"]
#
#qwen_framing = (qwen_neutral.groupby("Initial Framing")["Global Similarity To Original"].agg(["count", "mean", "median", "std"]).reset_index())
#llama_framing = (llama_neutral.groupby("Initial Framing")["Global Similarity To Original"].agg(["count", "mean", "median", "std"]).reset_index())
#
#print("\nQwen by framing:")
#print(qwen_framing.to_string(index=False))
#
#print("\nLlama by framing:")
#print(llama_framing.to_string(index=False))
#
#framing_comparison = qwen_framing[
#    ["Initial Framing", "mean"]
#].rename(columns={"mean": "Qwen Mean"})
#
#framing_comparison = framing_comparison.merge(
#    llama_framing[
#        ["Initial Framing", "mean"]
#    ].rename(columns={"mean": "Llama Mean"}),
#    on = "Initial Framing"
#)
#
#framing_comparison["Difference"] = (
#    framing_comparison["Llama Mean"]
#    - framing_comparison["Qwen Mean"]
#)
#
#print("\nQwen vs Llama by framing:")
#print(framing_comparison.to_string(index=False))
#
#framing_comparison.to_csv("neutral_QwenVLlama_comparion_by_framing.csv", index= False, )
#
#qwen_depth = pd.read_csv("GlobalVsLocalSemantic/global_Qwen_Similarity_Summary.csv")
#llama_depth = pd.read_csv("GlobalVsLocalSemantic/global_Llama_Similarity_Summary.csv")
#
#qwen_depth = qwen_depth.sort_values("Propagation Depth")
#llama_depth = llama_depth.sort_values("Propagation Depth")
#
#qwen_depth["Change From Previous"] = qwen_depth["mean"].diff()
#llama_depth["Change From Previous"] = llama_depth["mean"].diff()
#
#print("\nQwen change between depths:")
#print(qwen_depth[
#    ["Propagation Depth", "mean", "Change From Previous"]
#].to_string(index=False)
#)
#
#qwen_depth[
#    ["Propagation Depth", "mean", "Change From Previous"]
#].to_csv("qwen_propagation_evolution_change.csv")
#
#print("\nLlama change between depths:")
#print(llama_depth[
#    ["Propagation Depth", "mean", "Change From Previous"]
#].to_string(index=False)
#)
#
#llama_depth[
#    ["Propagation Depth", "mean", "Change From Previous"]
#].to_csv("llama_propagation_evolution_change.csv")

#qwen_semantic_shift_by_role = (qwen.groupby(["Propagation Depth", "Role selection"])
#    ["Similarity To Previous"]
#    .mean()
#    .unstack("Role selection")
#    .reset_index()
#)
#
##global_llama = (llama.groupby("Propagation Depth")["Global Similarity To Original"].agg(["count", "mean", "median", "std"]).reset_index())
#
#qwen_semantic_shift_by_role = qwen_semantic_shift_by_role.round(3)
#
#print(qwen_semantic_shift_by_role)
#
#qwen_semantic_shift_by_role.to_csv("communication_behaviour_local_similarity.csv", index=False)
#

#text_global = (
#    qwen.groupby("Propagation Depth")
#    ["Global Similarity To Original"]
#    .agg(["count", "mean", "median", "std"])
#    .reset_index()
#)
#
#visual_global = (
#    visual.groupby("Propagation Depth")
#    ["Global Similarity To Original"]
#    .agg(["count", "mean", "median", "std"])
#    .reset_index()
#)
#
#text_visual_global = text_global[
#    ["Propagation Depth", "mean"]
#].rename(columns={"mean": "Textual Mean"})
#
#text_visual_global = text_visual_global.merge(
#    visual_global[
#        ["Propagation Depth", "mean"]
#    ].rename(columns={"mean": "Multimodal Mean"}),
#    on="Propagation Depth",
#    how="outer"
#)
#
#text_visual_global["Differences"] = (
#    text_visual_global["Multimodal Mean"]
#    - text_visual_global["Textual Mean"]
#)
#
#print(text_visual_global)
#
#text_visual_global.to_csv("multimodal_global_sentiment_eval.csv")

#text_local = (
#    qwen.groupby("Propagation Depth")
#    ["Similarity To Previous"]
#    .agg(["count", "mean", "median", "std"])
#    .reset_index()
#)
#
#visual_local = (
#    visual.groupby("Propagation Depth")
#    ["Similarity To Previous"]
#    .agg(["count", "mean", "median", "std"])
#    .reset_index()
#)
#
#text_visual_local = text_local[
#    ["Propagation Depth", "mean"]
#].rename(columns={"mean": "Textual Mean"})
#
#text_visual_local = text_visual_local.merge(
#    visual_local[
#        ["Propagation Depth", "mean"]
#    ].rename(columns={"mean": "Multimodal Mean"}),
#    on="Propagation Depth",
#    how="outer"
#)
#
#text_visual_local["Differences"] = (
#    text_visual_local["Multimodal Mean"]
#    - text_visual_local["Textual Mean"]
#)
#
#print(text_visual_local)
#
#text_visual_local.to_csv("multimodal_local_sentiment_eval.csv")

#text_story = (
#    qwen.groupby("Story ID")
#    ["Global Similarity To Original"]
#    .mean()
#    .reset_index(name = "Textual Mean")
#)
#
#visual_story = (
#    visual.groupby("Story ID")
#    ["Global Similarity To Original"]
#    .mean()
#    .reset_index(name = "Multimodal Mean")
#)
#
#story_comparison = text_story.merge(
#    visual_story,
#    on="Story ID"
#)
#
#story_comparison["Difference"] = (
#    story_comparison["Multimodal Mean"]
#    - story_comparison["Textual Mean"]
#)
#
#print(story_comparison)
#
#story_comparison.to_csv("multimodal_story_comparison.csv")

#Headline vs full article using Llama

llama_quantity = llama[llama["Story ID"].isin([7,8,9])].copy()
article_llama = llama_article[llama_article["Story ID"].isin([7,8,9])].copy()

qwen_quantity = visual[visual["Story ID"].isin([7,8,9])].copy()
article_qwen = visual_article[visual_article["Story ID"].isin([7,8,9])].copy()

llama_headline_stats = (
    llama_quantity
    .groupby("Propagation Depth")["Global Similarity To Original"]
    .agg(["count", "mean", "median", "std"])
    .reset_index()
)

vision_headline_stats = (
    qwen_quantity
    .groupby("Propagation Depth")["Global Similarity To Original"]
    .agg(["count", "mean", "median", "std"])
    .reset_index()
)

llama_article_stats = (
    article_llama
    .groupby("Propagation Depth")["Global Similarity To Original"]
    .agg(["count", "mean", "median", "std"])
    .reset_index()
)

vision_article_stats = (
    article_qwen
    .groupby("Propagation Depth")["Global Similarity To Original"]
    .agg(["count", "mean", "median", "std"])
    .reset_index()
)

print("\nQwen - headline:")
print(vision_headline_stats.to_string(index=False))

print("\nQwen - full article:")
print(vision_article_stats.to_string(index=False)) 

#quantity_comparison = llama_headline_stats[
#    ["Propagation Depth", "mean", "median"]
#].rename(columns={
#    "mean": "Headline Mean",
#    "median": "Headline Median"
#})
#
#quantity_comparison = quantity_comparison.merge(
#    llama_article_stats[
#        ["Propagation Depth", "mean", "median"]
#    ].rename(columns={
#        "mean": "Article Mean",
#        "median": "Article Median"
#    }),
#    on = "Propagation Depth"
#)
#
#quantity_comparison["Difference"] = (
#    quantity_comparison["Article Mean"]
#    - quantity_comparison["Headline Mean"]
#)
#
#print("\nHeadline vs Full Article - Llama:")
#print(quantity_comparison.to_string(index= False))
#
#quantity_comparison.to_csv("llama_quantity_comparison.csv")

#Headline vs full article using multimodal 