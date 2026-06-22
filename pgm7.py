from transformers import T5ForConditionalGeneration, T5Tokenizer

tokenizer = T5Tokenizer.from_pretrained("t5-small")
model = T5ForConditionalGeneration.from_pretrained("t5-small")

text = """
The Industrial Revolution, which took place from the 18th to the 19th centuries, was a period during which predominantly agrarian, rural societies in Europe and America became industrial and urban. Prior to the Industrial Revolution, manufacturing was often done in people's homes, using hand tools or basic machines. Industrialization marked a shift to powered, special-purpose machinery, factories and mass production. The iron and textile industries, along with the development of the steam engine, played central roles in the Industrial Revolution, which also saw improved systems of transportation, communication and banking. While industrialization brought about an increased volume and variety of manufactured goods and an improved standard of living for some, it also resulted in often grim employment and living conditions for the poor and working classes.
"""

input_text = "summarize: " + text
input_ids = tokenizer.encode(input_text, return_tensors="pt", max_length=512, truncation=True)
summary_ids = model.generate(input_ids, max_length=60, min_length=30, do_sample=False)
summary_text = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
print("Generated Summary:")
print(summary_text)