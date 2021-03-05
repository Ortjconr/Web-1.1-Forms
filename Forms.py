@app.route('/froyo')
def choose_froyo():
    """Shows a form to collect the user's Fro-Yo order."""
    return """
    <form action="/froyo_results" method="GET">
        What if your favorite Fro-Yo flavor? <br/>
        <input type="text" name="flavor"><br/>
        <input type="text" name="toppings">br/>
        <input type="submit" value="Submit!">
    </form>
    """

@app.route('/froyo_results')
def show_froyo_results():
    users_froyo_flavor = request.args.get('flavor')
    users_froyo_flavor = request.args.get('toppings')
    return f'You ordered {users_froyo_flavor} flavored Fro-Yo!'
