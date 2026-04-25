# TODO.md

my todo.md

### Todo

- [ ] Fix game-end handling in reveal flow
  - [ ] Update apply_reveal() so that after flood_fill() it checks state["game_over"] and returns "break" when the board is already solved.
  - [ ] Add a defensive guard in make_heuristic() for the case where there are no valid candidate tiles.
- [ ] Simplify heuristic control flow
  - [ ] Refactor make_heuristic() so it only returns an int index.
  - [ ] Remove the old "continue" return path from make_heuristic().

### In Progress

- [ ] ...

### Done ✓

- [x] create testing space
- [x] add unit tests
  - [x] add github action to auto run unit tests after push/commit  