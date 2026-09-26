import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, RegularPolygon
from matplotlib.path import Path
from matplotlib.projections.polar import PolarAxes
from matplotlib.projections import register_projection
from matplotlib.spines import Spine
from matplotlib.transforms import Affine2D

def radar_factory(num_vars, frame='circle'):
    theta = np.linspace(0, 2*np.pi, num_vars, endpoint=False)

    class RadarAxes(PolarAxes):
        name = 'radar'
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.set_theta_zero_location('N')

        def fill(self, *args, closed=True, **kwargs):
            return super().fill(closed=closed, *args, **kwargs)

        def plot(self, *args, **kwargs):
            lines = super().plot(*args, **kwargs)
            for line in lines:
                self._close_line(line)

        def _close_line(self, line):
            x, y = line.get_data()
            if x[0] != x[-1]:
                x = np.concatenate((x, [x[0]]))
                y = np.concatenate((y, [y[0]]))
                line.set_data(x, y)

        def set_varlabels(self, labels, scores=None):
            self.set_thetagrids(np.degrees(theta), labels, color='#c9d1d9', fontsize=10, weight='bold')
            if scores:
                for ax, label, score in zip(self.get_xticklabels(), labels, scores):
                    ax.set_text(f"{label}\n{score}")
                    ax.set_horizontalalignment('center')

        def _gen_axes_patch(self):
            if frame == 'circle':
                return Circle((0.5, 0.5), 0.5)
            elif frame == 'polygon':
                return RegularPolygon((0.5, 0.5), num_vars, radius=0.5, edgecolor="k")
            else:
                raise ValueError("Unknown value for 'frame': %s" % frame)

        def _gen_axes_spines(self):
            if frame == 'circle':
                return super()._gen_axes_spines()
            elif frame == 'polygon':
                spine = Spine(axes=self, spine_type='circle', path=Path.unit_regular_polygon(num_vars))
                spine.set_transform(Affine2D().scale(.5).translate(.5, .5) + self.transAxes)
                return {'polar': spine}
            else:
                raise ValueError("Unknown value for 'frame': %s" % frame)

    register_projection(RadarAxes)
    return theta

def create_radar_chart(title, labels, scores, filename):
    N = len(labels)
    theta = radar_factory(N, frame='polygon')
    
    fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(projection='radar'))
    fig.patch.set_facecolor('#0d1117') # GitHub dark mode background
    ax.set_facecolor('#0d1117')
    
    ax.plot(theta, scores, color='#39d353', linewidth=2)
    ax.fill(theta, scores, color='#238636', alpha=0.2)
    
    ax.set_varlabels(labels, scores)
    ax.set_rgrids([20, 40, 60, 80, 100], labels=['', '', '', '', ''], color='#30363d', angle=0)
    ax.spines['polar'].set_color('#30363d')
    ax.tick_params(pad=20)
    ax.grid(color='#30363d', linestyle='-', linewidth=1)
    ax.set_ylim(0, 100)
    
    plt.title(title, color='#ffffff', size=14, weight='bold', y=1.1)
    
    # Save as transparent SVG
    plt.savefig(filename, format='svg', transparent=True, bbox_inches='tight', facecolor=fig.get_facecolor(), edgecolor='none')
    plt.close()

# Chart 1: Skill Radar
labels_1 = ['Blockchain / Web3', 'Stellar / Soroban', 'Smart Contracts', 'Next.js / React', 'TypeScript', 'Wallet Architecture', 'Digital Assets Infra']
scores_1 = [95, 80, 90, 85, 88, 75, 82]
create_radar_chart('Skill Radar', labels_1, scores_1, 'skill_radar.svg')

# Chart 2: Contract & Language Stack
labels_2 = ['Solidity', 'Smart Contracts', 'Move', 'Rust', 'TypeScript', 'JavaScript']
scores_2 = [85, 82, 72, 74, 88, 80]
create_radar_chart('Contract & Language Stack', labels_2, scores_2, 'language_stack.svg')

print("Radar SVGs generated successfully.")
