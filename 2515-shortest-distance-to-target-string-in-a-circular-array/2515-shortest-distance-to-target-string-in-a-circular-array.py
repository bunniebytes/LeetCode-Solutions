class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        hash_map = {k:v for k, v in enumerate(words) if v == target}
        len_words = len(words)
        min_step = None
        if not hash_map:
            return -1

        for k in hash_map.keys():
            if min_step is None:
                min_step = abs(startIndex - k)
            step_forward = abs(len_words - startIndex + k)
            step_backward = abs(len_words - k + startIndex)
            min_step = min(min_step, step_forward, step_backward, abs(startIndex - k))
        # step forward on other side of loop = len - given index + known index
        # step backward on other side of loop = len - known index + given index

        return min_step