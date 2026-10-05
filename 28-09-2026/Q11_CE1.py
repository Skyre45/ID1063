import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Patch
from matplotlib.lines import Line2D

# System A x = 0
A = np.array([[1, 1, 1],
              [1, 0, 2]])
d = np.cross(A[0], A[1])          # direction of intersection line
d = -d if d[0] > 0 else d         # (-2, 1, 1)
assert np.allclose(A @ d, 0)                  # direction satisfies both equations
assert np.allclose(A @ np.zeros(3), 0)        # origin satisfies both equations

x, y = np.meshgrid(np.linspace(-4, 4, 40), np.linspace(-4, 4, 40))
z1 = -x - y          # x1 + x2 + x3 = 0
z2 = -x / 2          # x1 + 2 x3 = 0
z1 = np.where(np.abs(z1) <= 4, z1, np.nan)    # keep planes inside the plot box

t = np.linspace(-2, 2, 200)
line = np.outer(d, t)

fig = plt.figure(figsize=(9, 8))
ax = fig.add_subplot(projection="3d")
ax.plot_surface(x, y, z1, alpha=0.30, color="tab:blue", linewidth=0)
ax.plot_surface(x, y, z2, alpha=0.30, color="tab:orange", linewidth=0)

# coordinate axes through the origin (dashed) so it's clear where (0,0,0) is
for v, lab in zip(np.eye(3), ["$x_1$", "$x_2$", "$x_3$"]):
    ax.plot(*(np.outer(v, [-4, 4])), color="gray", ls="--", lw=0.8)
    ax.text(*(4.3 * v), lab, color="gray")

# intersection line
ax.plot(*line, color="red", lw=3.5, zorder=10)
ax.text(*(1.5 * d) + np.array([0, 0.3, 0.6]),
        r"Line: $\mathbf{x}=t\,(-2,\,1,\,1)^\top$",
        color="red", fontsize=12, fontweight="bold",
        bbox=dict(fc="white", ec="red", alpha=0.85, boxstyle="round"))

# origin
ax.scatter(0, 0, 0, color="k", s=120, depthshade=False, zorder=20)
from mpl_toolkits.mplot3d import proj3d
X, Y, _ = proj3d.proj_transform(0, 0, 0, ax.get_proj())
ax.annotate("Origin (0, 0, 0)\nlies on both planes (t = 0)", xy=(X, Y), xycoords="data",
            xytext=(-120, -110), textcoords="offset points", fontsize=10,
            bbox=dict(fc="white", ec="k", boxstyle="round"),
            arrowprops=dict(arrowstyle="-|>", color="k", lw=1.5))

ax.set_xlim(-4, 4); ax.set_ylim(-4, 4); ax.set_zlim(-4, 4)
ax.set_xlabel("$x_1$"); ax.set_ylabel("$x_2$"); ax.set_zlabel("$x_3$")
ax.set_title("Two planes through the origin meet in a line")
ax.legend(handles=[
    Patch(color="tab:blue", alpha=0.4, label=r"Plane 1: $x_1+x_2+x_3=0$"),
    Patch(color="tab:orange", alpha=0.4, label=r"Plane 2: $x_1+2x_3=0$"),
    Line2D([0], [0], color="red", lw=3, label="Intersection line"),
    Line2D([0], [0], marker="o", color="k", ls="", label="Origin"),
], loc="upper left")
ax.view_init(elev=22, azim=-55)
fig.canvas.draw()

plt.savefig("Q11.png", dpi=250, bbox_inches="tight")
