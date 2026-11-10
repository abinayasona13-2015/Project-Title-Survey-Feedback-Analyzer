# ==========================================
# SURVEY FEEDBACK ANALYZER (Non-Interactive Version)
# ==========================================

# --- STEP 1: Preloaded Feedback Data ---
feedback_data = {
    'S_No': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Name': ['Ravi', 'Meera', 'Sam', 'Anu', 'Raj', 'Divya', 'Arjun', 'Kiran', 'Leela', 'Nisha'],
    'Feedback': [
        ' Very GOOD Service!!!',
        'poor support, not happy ',
        'GREAT experience! will come again.',
        'okay okay...',
        ' not BAD',
        'Excellent care, excellent staff!',
        'good food and good ambience!',
        'Poor response and poor handling of issue',
        'Satisfied. But could be better.',
        'Good support... quick service.'
    ],
    'Rating': [5, 2, 5, 3, 2, 5, 4, 1, 3, 4]
}
# --- STEP 2: Add More Feedbacks (Pre-defined to avoid terminal bugs) ---
new_feedbacks = [
    {"Name": "Rahul", "Feedback": "Amazing quality and fast delivery!", "Rating": 5},
    {"Name": "Priya", "Feedback": "Bad experience, very rude staff.", "Rating": 1}
]

start_sno = feedback_data['S_No'][-1] + 1

for item in new_feedbacks:
    feedback_data['S_No'].append(start_sno)
    feedback_data['Name'].append(item["Name"])
    feedback_data['Feedback'].append(item["Feedback"])
    feedback_data['Rating'].append(item["Rating"])
    start_sno += 1

print("✅ STEP 2 Complete: New feedbacks added automatically!")

# --- STEP 3: Text Cleaning ---
cleaned_feedback_list = []
for text in feedback_data['Feedback']:
    text = text.lower()
    for punct in ['.', ',', '!', '?']:
        text = text.replace(punct, '')
    cleaned_text = ' '.join(text.split())
    cleaned_feedback_list.append(cleaned_text)

feedback_data['Cleaned_Feedback'] = cleaned_feedback_list
print("✅ STEP 3 Complete: All feedbacks cleaned successfully!")

# --- STEP 4: Word Count Insights ---
def count_word_in_feedbacks(word):
    target = word.lower().strip()
    count = 0
    for feedback in feedback_data['Cleaned_Feedback']:
        if target in feedback.split():
            count += 1
    return count

print("\n--- STEP 4: Word Count Results ---")
print(f"Feedbacks containing 'good'      : {count_word_in_feedbacks('good')}")
print(f"Feedbacks containing 'poor'      : {count_word_in_feedbacks('poor')}")
print(f"Feedbacks containing 'excellent' : {count_word_in_feedbacks('excellent')}")

# --- STEP 5: Final Summary & Insights ---
print("\n--- STEP 5: Final Summary & Insights ---")
avg_rating = sum(feedback_data['Rating']) / len(feedback_data['Rating'])
print(f"📊 Average Rating: {avg_rating:.2f} / 5.0")

# Unique Words
unique_words = set()
for text in feedback_data['Cleaned_Feedback']:
    for word in text.split():
        unique_words.add(word)
print(f"🔤 Total Unique Words Used: {len(unique_words)}")

# Sort by Rating
combined = list(zip(feedback_data['S_No'], feedback_data['Name'], feedback_data['Feedback'], feedback_data['Rating']))
sorted_feedbacks = sorted(combined, key=lambda x: x[3], reverse=True)

print("\n" + "="*50)
print("🧩 Sorted Feedbacks (Highest Rating First):")
print("="*50)
for sno, name, fb, rating in sorted_feedbacks:
    print(f"S.No: {sno:<3} | Name: {name:<8} | Rating: {rating} | Feedback: {fb.strip()}")
print("="*50)

