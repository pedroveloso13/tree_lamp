#it needs grasshopper inputs to work
import rhinoscriptsyntax as rs
import Rhino.Geometry as rg
import random
import rhinoscriptsyntax as rs
from Grasshopper.Kernel.Data import GH_Path
from Grasshopper import DataTree

lights = []
base_tree.Clear()
tree = base_tree

def createBranch(base_branch, cur_len, max_ang, num, ang):
    ang_cone = max_ang + random.randrange(-10, 11) / 10 * rand_factor * max_ang / 2
    ang_plane = num * ang + random.randrange(-10, 11) / 10 * rand_factor * ang / 2
    old_vector=rs.VectorCreate(base_branch.To, base_branch.From)
    new_vector = rs.VectorUnitize(old_vector)
    new_vector = rs.VectorScale(new_vector, cur_len)
    MutationPlane = rs.PlaneFromNormal((0,0,0), new_vector)
    new_vector = rs.VectorRotate(new_vector, ang_cone, MutationPlane.YAxis)
    new_vector = rs.VectorRotate(new_vector, ang_plane, old_vector)
    return rg.Line(base_branch.To, new_vector)
    #return rs.AddLine(base_branch.To, base_branch.To + new_vector)

root_branch = rg.Line(rg.Point3d(0,0, -10), rg.Point3d(0, 0, 0))
base_branches=[]
cur_branches=[]
all_branches=[]
total_fac = 0
for i in xrange(gen):
    total_fac += factor ** i
cur_len = max_len / total_fac
first_branch = createBranch(root_branch, cur_len, rand_factor * random.random() * 20, 0, 360 )
all_branches.append(rs.coerceline(first_branch))
base_branches.append(rs.coerceline(first_branch))
path = GH_Path(0)
tree.Add(first_branch, path)

for i in xrange(1,gen):
    cur_len *= (factor + factor * random.randrange(-2, 2) / 10 * rand_factor)
    path = GH_Path(i)
    for j in xrange(0,len(base_branches)):
        new_range = max(1, max_branch + random.randrange(-2, 2) * rand_factor)
        for k in xrange (0, new_range):
            ang = 360 / max_branch
            new_branch = createBranch(base_branches[j], cur_len, max_ang, k, ang )
            if i == gen - 1:
                lights.append(new_branch.PointAt(1.0))
            cur_branches.append(new_branch)
            tree.Add(new_branch, path)
    base_branches = cur_branches
    for branch in cur_branches:
        all_branches.append(branch)
    cur_branches=[]
