def compute_q_value(transition, model):
    if transition.state.speed == 0:
        return transition.reward
    else:
        q_values = model.predict([[transition]])
        return transition.reward + max(q_values)
