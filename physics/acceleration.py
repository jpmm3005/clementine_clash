import numpy as np
from scipy.integrate import solve_ivp
import plotly.graph_objects as go


g       = 9.81          # gravitational acceleration (m s‑2)
t_span  = (0, 4)        # time window (s)
y0      = [0.0, 20.0]   # initial [position (m), velocity (m s‑1)]
n_steps = 300           # resolution of the solution grid


def rhs(t, y, g):
    """
    y = [x, v]   ‑>   dy/dt = [ v,  -g ]
    (second‑order ODE written as first‑order system)
    """
    return [y[1], -g]

# solve the IVP
t_eval = np.linspace(*t_span, n_steps)
sol = solve_ivp(rhs, t_span, y0, t_eval=t_eval, args=(g,))

# --- Plotly figure --------------------------------------
fig = go.Figure()

# position trace
fig.add_trace(go.Scatter(
    x=sol.t, y=sol.y[0],
    mode="lines", name="position  x(t)  [m]"
))

# velocity trace on a secondary y‑axis
fig.add_trace(go.Scatter(
    x=sol.t, y=sol.y[1],
    mode="lines", name="velocity  v(t)  [m s⁻¹]",
    yaxis="y2"
))

# layout tweaks
fig.update_layout(
    title="Projectile under constant gravity  (ODE:  x''(t) = –g )",
    xaxis_title="time  t  [s]",
    yaxis=dict(title="position  x  [m]"),
    yaxis2=dict(title="velocity  v  [m s⁻¹]",
                overlaying="y", side="right", showgrid=False),
    legend=dict(x=0.02, y=0.98),
    template="plotly_white",
    annotations=[dict(
        x=0.5*(t_span[1]-t_span[0]),
        y=max(sol.y[0]),  # place at top of trajectory
        text=" $\\displaystyle x''(t) = -g$ ",
        showarrow=False,
        font=dict(size=14)
    )]
)

fig.savefig('acceleration.png')