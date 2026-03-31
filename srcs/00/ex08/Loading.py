def ft_tqdm(lst: range) -> None:
    max_characters = 80
    n = 0
    for i in lst:
        n += 1
        percent = int(n / len(lst) * 100)
        limit = int(percent / 100 * max_characters)
        progress = "█" * limit + " " * (max_characters - limit)
        per_str = f"{' '* (3 - len(str(percent)))}{percent}%"
        print(f"\r{per_str}|{progress}| {n}/{len(lst)}", end="", flush=True)
        yield i
    print()
