def extract_model_answer(response):
    if "<answer>" not in response or "</answer>" not in response:
        return None
    after_open = response.split("<answer>")[1]
    inside = after_open.split("</answer>")[0]
    return inside.strip().replace(",", "")

def correctness_reward(response,ground_truth):
    a = extract_model_answer(response)
    if a is None:
        return 0
    try:
        a =float(a)
        ground_truth = float(ground_truth)
    except ValueError:
        return 0

    if a==ground_truth:
        return 1
    else:
        return 0
print(correctness_reward("<answer>72 clips</answer>","72"))
