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

def format_reward(response):
    a = extract_model_answer(response)
    if a is None:
        return 0
    else:
        return 0.15

def total_reward(response, ground_truth):
    a = format_reward(response) + correctness_reward(response,ground_truth)
    return a



    
# tests = [
#     ("The total is 72.", "72", 0),
#     ("<answer>17</answer>", "72", 0.15),
#     ("The total is 72. <answer>72</answer>", "72", 1.15),
#     ("<answer>$72</answer>", "72", 0.15),
# ]

# for response, truth, expected in tests:
#     got = total_reward(response, truth)
#     print(response, "| expected:", expected, "| got:", got)


