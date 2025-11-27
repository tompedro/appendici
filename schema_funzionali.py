import matplotlib.pyplot as plt
import matplotlib.patches as patches

def draw_final_hierarchy_intersection_fixed():
    fig, ax = plt.subplots(figsize=(20, 18))
    ax.set_xlim(-14, 14)
    ax.set_ylim(-14, 14)
    ax.axis('off')
    
    # --- CONFIG STILI ---
    style_label = dict(boxstyle="round,pad=0.4", fc="white", ec="black", alpha=1.0, zorder=150)

    # Arrowprops di base
    base_arrow = dict(arrowstyle="->", color='black', lw=1.5, shrinkA=5, shrinkB=5)

    # Funzione che alza TUTTE le frecce sopra agli insiemi
    def high_arrow(**kwargs):
        d = base_arrow.copy()
        d.update(kwargs)
        d["zorder"] = 200      # <<< LA CHIAVE CHE RISOLVE TUTTO
        return d

    # --- SFONDO DISTRIBUZIONI ---
    rect_dist = patches.FancyBboxPatch(
        (-13, -13), 26, 26, boxstyle="round,pad=0.2",
        fc='#f5f5f5', ec='#cccccc', linestyle='--', zorder=1
    )
    ax.add_patch(rect_dist)
    ax.text(-12.5, -12.5, "Universo $\mathcal{D}'$ (Distribuzioni Generiche)", 
            fontsize=14, color='gray', ha='left', va='bottom', zorder=5)

    # --- S' ---
    s_prime_patch = patches.Ellipse((0, -1), 24, 20,
                                    fc='#ede7f6', ec='#673ab7', alpha=0.5, zorder=10)
    ax.add_patch(s_prime_patch)

    ax.annotate("$\\mathcal{S}'$ (Temperate)",
                xy=(-9, 6), xytext=(-12, 9),
                arrowprops=high_arrow(color="#673ab7", lw=2, connectionstyle="arc3,rad=0.2"),
                fontsize=14, color='#5e35b1', fontweight='bold', bbox=style_label)

    # --- L^1_loc ---
    l1loc_patch = patches.Ellipse((-3, 0), 20, 26,
                                  fc='#e0f7fa', ec='#006064', linestyle='-.',
                                  lw=2, alpha=0.4, zorder=15)
    ax.add_patch(l1loc_patch)

    # --- C^0, L^inf, L^1, L^2 ---
    c0_patch = patches.Ellipse((0, 0), 11, 23, fc='#fff3e0', ec='#ef6c00', alpha=0.5, zorder=20)
    ax.add_patch(c0_patch)

    linf_patch = patches.Ellipse((-1.5, -1), 15, 7, fc='#ffebee', ec='#c62828', alpha=0.5, zorder=22)
    ax.add_patch(linf_patch)

    l1_patch = patches.Ellipse((-2, -2), 9, 7, angle=45,
                               fc='#e8f5e9', ec='#2e7d32', alpha=0.6, zorder=23)
    ax.add_patch(l1_patch)

    l2_patch = patches.Ellipse((0, -0.5), 8, 8,
                               fc='#e8eaf6', ec='#3f51b5', alpha=0.5, zorder=25)
    ax.add_patch(l2_patch)

    # --- C^1, C^k, C^∞ ---
    c1_patch = patches.Ellipse((0, 0), 8.5, 23,
                               fc='#ffe0b2', ec='#ffa726', alpha=0.4, zorder=26)
    ax.add_patch(c1_patch)

    ck_patch = patches.Ellipse((0, 0), 6.5, 23,
                               fc='#ffcc80', ec='#fb8c00', alpha=0.4, zorder=27)
    ax.add_patch(ck_patch)

    cinf_patch = patches.Ellipse((0, 0), 4.5, 23,
                                 fc='#e0f2f1', ec='#00695c', alpha=0.5, zorder=29)
    ax.add_patch(cinf_patch)

    # --- Schwartz S ---
    schwartz_patch = patches.Ellipse((0, -0.5), 2.5, 9.0,
                                     fc='#f8bbd0', ec='#c2185b', lw=2, alpha=0.9, zorder=50)
    ax.add_patch(schwartz_patch)

    # --- E' ---
    eprime_patch = patches.Ellipse((3.5, -0.5), 9.5, 2.8,
                                   fc='#d7ccc8', ec='#5d4037', linestyle='--',
                                   lw=2, alpha=0.8, zorder=51)
    ax.add_patch(eprime_patch)

    # --- H^1, H^s ---
    h1_patch = patches.Circle((0, -0.5), 2.8,
                              fc='#7986cb', ec='#1a237e', alpha=0.8, zorder=60)
    ax.add_patch(h1_patch)

    hs_patch = patches.Circle((0, -0.5), 1.2,
                              fc='#304ffe', ec='white', alpha=1.0, zorder=61)
    ax.add_patch(hs_patch)

    # --- C0^∞ ---
    c0inf_patch = patches.Circle((0, -0.5), 0.6,
                                 fc='#ffeb3b', ec='black', zorder=70)
    ax.add_patch(c0inf_patch)

    # --- LABEL E FRECCE (TUTTE con high_arrow) ---

    ax.annotate(r"$L^1_{loc}$",
                xy=(-6, 10), xytext=(-12, 12),
                arrowprops=high_arrow(color="#006064", lw=2, connectionstyle="arc3,rad=0.2"),
                fontsize=14, color='#006064', fontweight='bold', bbox=style_label)

    ax.annotate(r"$C^0$",
                xy=(5, 8), xytext=(10, 8),
                arrowprops=high_arrow(connectionstyle="arc3,rad=0.2"),
                fontsize=14, color='#e65100', fontweight='bold', bbox=style_label)

    ax.annotate(r"$C^k$",
                xy=(3.2, 9), xytext=(10, 5),
                arrowprops=high_arrow(connectionstyle="arc3,rad=0.2"),
                fontsize=12, bbox=style_label)

    ax.annotate(r"$C^\infty$",
                xy=(0, 11), xytext=(-6, 11.5),
                arrowprops=high_arrow(connectionstyle="arc3,rad=-0.1"),
                fontsize=12, color='#004d40', fontweight='bold', bbox=style_label)

    ax.annotate(r"$L^\infty$",
                xy=(9, -1), xytext=(11, 1),
                arrowprops=high_arrow(connectionstyle="arc3,rad=0.2"),
                fontsize=13, color='#b71c1c', fontweight='bold', bbox=style_label)

    ax.annotate(r"$L^1$",
                xy=(-3, -3), xytext=(-11, -5),
                arrowprops=high_arrow(connectionstyle="arc3,rad=0.1"),
                fontsize=13, color='#1b5e20', fontweight='bold', bbox=style_label)

    ax.annotate(r"$L^2$",
                xy=(3, -3), xytext=(9, -6),
                arrowprops=high_arrow(connectionstyle="arc3,rad=0.2"),
                fontsize=13, color='#1a237e', fontweight='bold', bbox=style_label)

    ax.annotate(r"$H^1$",
                xy=(1.5, -1.5), xytext=(7, -9),
                arrowprops=high_arrow(connectionstyle="arc3,rad=0.3"),
                fontsize=12, color='white', fontweight='bold',
                bbox=dict(boxstyle="round,pad=0.4", fc="#304ffe", ec="black", alpha=1))

    ax.annotate(r"$\mathcal{S}$",
                xy=(0, 2.5), xytext=(-4, 6),
                arrowprops=high_arrow(color="#c2185b", lw=2, connectionstyle="arc3,rad=0.1"),
                fontsize=14, color='#c2185b', fontweight='bold',
                bbox=dict(boxstyle="round,pad=0.4", fc="white", ec="#c2185b", zorder=150))

    ax.annotate(r"$\mathcal{E}'$",
                xy=(6, -0.5), xytext=(10, 3),
                arrowprops=high_arrow(color="#5d4037", lw=2, connectionstyle="arc3,rad=-0.2"),
                fontsize=13, color='#5d4037', fontweight='bold',
                bbox=dict(boxstyle="round,pad=0.4", fc="white", ec="#5d4037", zorder=150))

    ax.annotate(r"$C_0^\infty$",
                xy=(0, -0.5), xytext=(-10, 1),
                arrowprops=high_arrow(connectionstyle="arc3,rad=0.1"),
                fontsize=14, fontweight='bold',
                bbox=dict(boxstyle="round,pad=0.4", fc="#fff176", ec="black", alpha=1, zorder=150))

    ax.annotate(r"$\delta$ (Dirac)\n(In $\mathcal{E}'$ ma fuori $L^1_{loc}$)",
                xy=(7.8, -0.5), xytext=(9, -4),
                arrowprops=high_arrow(color="red", lw=2, connectionstyle="arc3,rad=-0.2"),
                fontsize=12, color='#b71c1c', fontweight='bold',
                bbox=dict(boxstyle="round,pad=0.4", fc="#ffcdd2", ec="red", zorder=150))

    plt.title("Mappa Finale: $\mathcal{S}$ e $\mathcal{E}'$ si incrociano solo in $C_0^\infty$", fontsize=22, pad=20)
    plt.savefig("function_spaces_final_intersection_fixed.png", bbox_inches='tight', dpi=300)

draw_final_hierarchy_intersection_fixed()
