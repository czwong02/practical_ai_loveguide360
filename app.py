from jamaibase import JamAI, protocol as p
from flask import Flask, render_template, request, jsonify, redirect
import os
from dotenv import load_dotenv

app = Flask(__name__)

load_dotenv()

jamai = JamAI(
    api_key=os.getenv("JAMAI_API_KEY"),
    project_id=os.getenv("JAMAI_PROJECT_ID"),
)


@app.route("/", methods=["GET", "POST"])
def landing():
    if request.method == "POST":
        gender = request.form["gender"]
        age_group = request.form["age_group"]
        partner_gender = request.form["partner_gender"]
        partner_age_group = request.form["partner_age_group"]
        # Here you can save or use these values as needed
        return redirect(
            f"/index.html?gender={gender}&age_group={age_group}&partner_gender={partner_gender}&partner_age_group={partner_age_group}"
        )
    return render_template("landing.html")


@app.route("/index.html")
def index():
    gender = request.args.get("gender", "")
    age_group = request.args.get("age_group", "")
    partner_gender = request.args.get("partner_gender", "")
    partner_age_group = request.args.get("partner_age_group", "")
    return render_template(
        "index.html",
        gender=gender,
        age_group=age_group,
        partner_gender=partner_gender,
        partner_age_group=partner_age_group,
    )


@app.route("/process_conflict", methods=["POST"])
def process_conflict():
    result = {}

    # Retrieve form data
    category = request.form.get("category")

    gender = request.form.get("gender")
    age_group = request.form.get("age_group")
    partner_gender = request.form.get("partner_gender")
    partner_age_group = request.form.get("partner_age_group")

   # Relationship conflict
    years = request.form.get("years")
    love_language = request.form.get("love_language")
    conflict_type = request.form.get("conflict_type")
    conflict_frequency = request.form.get("conflict_frequency")
    partner_temperament = request.form.get("partner_temperament")
    your_temperament = request.form.get("your_temperament") 

    # Romantic Gestures
    zodiac = request.form.get("zodiac")
    occasion = request.form.get("occasion")
    preferences = request.form.get("preferences")
    budget = request.form.get("budget")
    environment = request.form.get("environment")
    past_gestures = request.form.get("past_gestures")

    # Long-Distance Relationship
    time_difference = request.form.get("time_difference")
    communication_style = request.form.get("communication_style")
    visit_frequency = request.form.get("visit_frequency")
    emotional_challenges = request.form.get("emotional_challenges")
    duration_separation = request.form.get("duration_separation")
    partner_availability = request.form.get("partner_availability")

    # Personal Growth and Relationship
    your_zodiac = request.form.get("your_zodiac")
    partner_zodiac = request.form.get("partner_zodiac")
    your_goals = request.form.get("your_goals")
    partner_goals = request.form.get("partner_goals")
    shared_hobbies = request.form.get("shared_hobbies")
    counseling_history = request.form.get("counseling_history")

    # Dating Advice
    date_type = request.form.get("date_type")
    location_preference = request.form.get("location_preference")
    first_date = request.form.get("first_date")
    previous_experiences = request.form.get("previous_experiences")
    chemistry_level = request.form.get("chemistry_level")
    partner_hobbies = request.form.get("partner_hobbies")

    # Communication Challenges
    argument_topic = request.form.get("argument_topic")
    communication_style = request.form.get("communication_style")
    partner_listening = request.form.get("partner_listening")
    your_listening = request.form.get("your_listening")
    argument_duration = request.form.get("argument_duration")
    conflict_resolution = request.form.get("conflict_resolution")

    # Trust Issues
    trust_type = request.form.get("trust_type")
    incident_history = request.form.get("incident_history")
    time_since = request.form.get("time_since")
    forgiveness_progress = request.form.get("forgiveness_progress")
    communication_efforts = request.form.get("communication_efforts")
    partner_behavior = request.form.get("partner_behavior")

    try:
        if category == 'conflict':
            completion = jamai.add_table_rows(
                "action",
                p.RowAddRequest(
                    table_id="conflict",
                    data=[
                        {
                            "gender": gender,
                            "age group": age_group,
                            "partner_gender": partner_gender,
                            "partner_age_group": partner_age_group,
                            "year together": years,
                            "love language": love_language,
                            "conflict type": conflict_type,
                            "conflict frequency": conflict_frequency,
                            "partner temperament": partner_temperament,
                            "your temperament": your_temperament
                        }
                    ],
                    stream=False,
                ),
            )

            response_list = ['summary', 'challenges', 'empathetic_insights', 'strategies_for_improvement', 'expected_outcomes', 'call_to_action']
            result = {}
            for x in response_list:
                response = extract_response_from_completion(completion, x)
                if response:
                    print("Extracted response:", response)
                    result[x] = response
                else:
                    print("No valid response was extracted.")

        elif category == 'romance':
            completion = jamai.add_table_rows(
                "action",
                p.RowAddRequest(
                    table_id="romance",
                    data=[
                        {
                            "gender": gender,
                            "age group": age_group,
                            "partner_gender": partner_gender,
                            "partner_age_group": partner_age_group,
                            "zodiac": zodiac,
                            "occasion": occasion,
                            "preferences": preferences,
                            "budget": budget,
                            "environment": environment,
                            "past gestures": past_gestures
                        }
                    ],
                    stream=False,
                ),
            )

            response_list = ['summary', 'challenges', 'romantic_gesture_ideas', 'strategies', 'expected_outcomes', 'call_to_action']
            result = {}
            for x in response_list:
                response = extract_response_from_completion(completion, x)
                if response:
                    print("Extracted response:", response)
                    result[x] = response
                else:
                    print("No valid response was extracted.")
        elif category == 'long_distance':
            completion = jamai.add_table_rows(
                "action",
                p.RowAddRequest(
                    table_id="long_distance",
                    data=[
                        {
                            "gender": gender,
                            "age group": age_group,
                            "partner_gender": partner_gender,
                            "partner_age_group": partner_age_group,
                            "time_difference": time_difference,
                            "communication_style": communication_style,
                            "visit_frequency": visit_frequency,
                            "emotional_challenges": emotional_challenges,
                            "duration_separation": duration_separation,
                            "partner_availability": partner_availability
                        }
                    ],
                    stream=False,
                ),
            )

            response_list = ['summary', 'challenges', 'empathetic_insights', 'strategies_for_improvement', 'expected_outcomes', 'call_to_action']
            result = {}
            for x in response_list:
                response = extract_response_from_completion(completion, x)
                if response:
                    print("Extracted response:", response)
                    result[x] = response
                else:
                    print("No valid response was extracted.")
        elif category == 'growth':
            completion = jamai.add_table_rows(
                "action",
                p.RowAddRequest(
                    table_id="growth",
                    data=[
                        {
                            "gender": gender,
                            "age group": age_group,
                            "partner_gender": partner_gender,
                            "partner_age_group": partner_age_group,
                            "your_zodiac": your_zodiac,
                            "partner_zodiac": partner_zodiac,
                            "your_goals": your_goals,
                            "partner_goals": partner_goals,
                            "shared_hobbies": shared_hobbies,
                            "counseling_history": counseling_history
                        }
                    ],
                    stream=False,
                ),
            )

            response_list = ['summary', 'challenges', 'empathetic_insights', 'strategies_for_improvement', 'expected_outcomes', 'call_to_action']
            result = {}
            for x in response_list:
                response = extract_response_from_completion(completion, x)
                if response:
                    print("Extracted response:", response)
                    result[x] = response
                else:
                    print("No valid response was extracted.")
        elif category == 'dating':
            completion = jamai.add_table_rows(
                "action",
                p.RowAddRequest(
                    table_id="dating",
                    data=[
                        {
                            "gender": gender,
                            "age group": age_group,
                            "partner_gender": partner_gender,
                            "partner_age_group": partner_age_group,
                            "date_type": date_type,
                            "location_preference": location_preference,
                            "first_date": first_date,
                            "previous_experiences": previous_experiences,
                            "chemistry_level": chemistry_level,
                            "partner_hobbies": partner_hobbies
                        }
                    ],
                    stream=False,
                ),
            )

            response_list = ['summary', 'challenges', 'empathetic_insights', 'strategies_for_improvement', 'expected_outcomes', 'call_to_action']
            result = {}
            for x in response_list:
                response = extract_response_from_completion(completion, x)
                if response:
                    print("Extracted response:", response)
                    result[x] = response
                else:
                    print("No valid response was extracted.")
        elif category == 'communication':
            completion = jamai.add_table_rows(
                "action",
                p.RowAddRequest(
                    table_id="communication",
                    data=[
                        {
                            "gender": gender,
                            "age group": age_group,
                            "partner_gender": partner_gender,
                            "partner_age_group": partner_age_group,
                            "argument_topic": argument_topic,
                            "communication_style": communication_style,
                            "partner_listening": partner_listening,
                            "your_listening": your_listening,
                            "argument_duration": argument_duration,
                            "conflict_resolution": conflict_resolution
                        }
                    ],
                    stream=False,
                ),
            )

            response_list = ['summary', 'challenges', 'empathetic_insights', 'strategies_for_improvement', 'expected_outcomes', 'call_to_action']
            result = {}
            for x in response_list:
                response = extract_response_from_completion(completion, x)
                if response:
                    print("Extracted response:", response)
                    result[x] = response
                else:
                    print("No valid response was extracted.")
        elif category == 'trust':
            completion = jamai.add_table_rows(
                "action",
                p.RowAddRequest(
                    table_id="trust",
                    data=[
                        {
                            "gender": gender,
                            "age group": age_group,
                            "partner_gender": partner_gender,
                            "partner_age_group": partner_age_group,
                            "trust_type": trust_type,
                            "incident_history": incident_history,
                            "time_since": time_since,
                            "forgiveness_progress": forgiveness_progress,
                            "communication_efforts": communication_efforts,
                            "partner_behavior": partner_behavior
                        }
                    ],
                    stream=False,
                ),
            )

            response_list = ['summary', 'challenges', 'empathetic_insights', 'strategies_for_improvement', 'expected_outcomes', 'call_to_action']
            result = {}
            for x in response_list:
                response = extract_response_from_completion(completion, x)
                if response:
                    print("Extracted response:", response)
                    result[x] = response
                else:
                    print("No valid response was extracted.")
        else:
            print("Invalid category")
        
    except Exception as e:
        print("error", e)

    return render_template("result.html", result=result, category=category)

def extract_response_from_completion(completion, response):
    if completion.rows:
        # Iterate over each row
        for row in completion.rows:
            # Access the columns dictionary
            columns = row.columns
            # Check if "response" is in columns
            if response in columns:
                # Extract the response column
                response_chunk = columns[response]
                # Extract choices from ChatCompletionChunk
                if response_chunk.choices:
                    # Get the first choice (can be adjusted as needed)
                    first_choice = response_chunk.choices[0]
                    # Extract the message content
                    if hasattr(first_choice, "message") and hasattr(first_choice.message, "content"):
                        return first_choice.message.content  # Return the actual response content
                    else:
                        print("Message content not found in the choice.")
                else:
                    print("No choices available in the response chunk.")
            else:
                print("Response column not found.")
    else:
        print("No rows found in the completion object.")
    
    # Return None if no valid response is found
    return None

if __name__ == "__main__":
    app.run(debug=True)
