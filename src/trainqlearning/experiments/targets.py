import numpy as np

def compute_q_value(transition, model, objective):
    if transition.state.speed == 0:
        return transition.reward
    else:
        record = compute_record(transition, objective)
        q_values = model.predict([record])
        return transition.reward + np.max(q_values)


def compute_record(transition, objective):
    position = transition.previous_state.position
    speed = transition.previous_state.speed
    objective = objective
    brake_power = transition.previous_brake_power
    return [position, speed, objective, brake_power]


def build_train_set(transitions, model, objective):
    y = []
    x = []
    for transition in transitions:
        y.append(compute_q_value(transition, model, objective))
        x.append(compute_record(transition, objective))
    return x, y


def mini_batch_train_set(episode):
    transitions = episode.record.get_last_transitions()
    train_set = build_train_set(transitions=transitions,
                                model=episode.model,
                                objective=episode.controler.objective)
    return train_set
