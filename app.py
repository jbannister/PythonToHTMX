from flask import Flask, request, render_template_string

app = Flask(__name__)

items = [
    {'id':"1234", "Name": "AAAA", "Active": True},
    {'id':"2345", "Name": "BBBB", "Active": True},
    {'id':"3456", "Name": "CCCC", "Active": True},
]

@app.route('/')
def index():
    return render_template_string(open('templates/index.html').read(), items=items)

@app.route('/add', methods=['POST'])
def add_item():
    content = request.form.get('content')
    if content:
        item = {'id':"1234", "Name": "....", "Active": True}
        items.append(item)
    return render_template_string(open('templates/items.html').read(), items=[item])

@app.route('/delete/<int:item_id>', methods=['POST'])
def delete_item(item_id):
    for x in items:
        if x['id'] == item_id:
            items.remove(item_id)
    return '', 204

# Add routes for updating items here

if __name__ == '__main__':
    app.run(debug=True)
