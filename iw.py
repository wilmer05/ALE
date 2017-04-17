from iterated_width import iterated_width_search
import MySearchModel
import searchspace

model = MySearchModel.MySearchModel(searchspace)
options = {
    'max_width' : 1
}
sol = iterated_width_search(None, options, model=model)

if sol:
    print "Solution found:"
    model.simulate_actions(sol)
else:
    print "No solution found"
