from flask import Flask, jsonify, request

app = Flask(__name__)

# Simulated data
class Event:
    def __init__(self, id, title):
        self.id = id
        self.title = title

    def to_dict(self):
        return {"id": self.id, "title": self.title}

events = [
    Event(1, "Tech Meetup"),
    Event(2, "Python Workshop")
]

# TODO: POST /events - Create a new event from JSON input
@app.route("/events", methods=["POST"])
def create_event():
    data = request.get_json()
    new_id = max([e.id for e in events]) + 1 if events else 1
    new_event = Event (id=new_id, title=data["title"])
    events.append(new_event)
    return jsonify(new_event.to_dict()), 201

# TODO: PATCH /events/<id> - Update the title of an event
@app.route("/events/<int:id>", methods=["PATCH"])
def update_event(id):
    data = request.get_json()
    event = next((e for e in events if e.id == id), None)
    if not event:
        return ("Event not found", 404)
    if "title" in data:
        event.title = data["title"]
    return jsonify(event.to_dict())

# TODO: DELETE /events/<id> - Remove an event from the list

if __name__ == "__main__":
    app.run(debug=True)