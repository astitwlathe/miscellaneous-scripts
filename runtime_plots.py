import pandas as pd
import matplotlib.pyplot as plt

ls_names = ["AdjDijkstra.csv", "AdjToposort.csv", "GenDijkstra.csv", "GenToposort.csv", "DynamicProgramming.csv"]
ls_df = []
for name in ls_names:
    ls_df.append(pd.read_csv(name, index_col=0, header=None, sep=","))    
# plt.xticks(fontsize=8, rotation=90)
# print(ls_df[0])
fig, axs = plt.subplots(5, figsize=(15))

# axs[0, 0].xticks(fontsize=8)
axs[0].plot(ls_df[0].index.to_numpy(), ls_df[0].iloc[:, 0].to_numpy())
axs[0].set(xlabel="N", ylabel="Time", title="AdjDijkstra")
axs[0].tick_params(axis='x', labelsize=8)
axs[0].tick_params(axis='y', labelsize=8)

axs[1].plot(ls_df[1].index.to_numpy(), ls_df[1].iloc[:, 0].to_numpy())
axs[1].set(xlabel="N", ylabel="Time", title="AdjToposort")
axs[1].tick_params(axis='x', labelsize=8)
axs[1].tick_params(axis='y', labelsize=8)

axs[2].plot(ls_df[2].index.to_numpy(), ls_df[2].iloc[:, 0].to_numpy())
axs[2].set(xlabel="N", ylabel="Time", title="GenDijkstra")
axs[2].tick_params(axis='x', labelsize=8)
axs[2].tick_params(axis='y', labelsize=8)


axs[3].plot(ls_df[3].index.to_numpy(), ls_df[3].iloc[:, 0].to_numpy())
axs[3].set(xlabel="N", ylabel="Time", title="GenToposort")
axs[3].tick_params(axis='x', labelsize=8)
axs[3].tick_params(axis='y', labelsize=8)

# fig.tight_layout()
# fig.subplots_adjust(top=0.88)
# fig.suptitle("Runtime", y=.98, x=.56)
# plt.savefig("addAll_plot.png")

# fig, axs = plt.subplots(1, 1)
axs[4].plot(ls_df[4].index.to_numpy(), ls_df[4].iloc[:, 0].to_numpy())
axs[4].set(xlabel="N", ylabel="Time", title="DynamicProgramming")
axs[4].tick_params(axis='x', labelsize=8)
axs[4].tick_params(axis='y', labelsize=8)


fig.tight_layout()
fig.subplots_adjust(top=0.88)
fig.suptitle("Runtime", y=.98, x=.56)
plt.savefig("addAll_plot3.png")





# fig, axs = plt.subplots(2, 2)
# # axs[0, 0].xticks(fontsize=8)
# axs[0, 0].plot(ls_df[0].index.to_numpy(), ls_df[0].iloc[:, 1].to_numpy())
# axs[0, 0].set(xlabel="N", ylabel="Time", title="Linear Search")
# axs[0, 0].tick_params(axis='x', labelsize=8)
# axs[0, 0].tick_params(axis='y', labelsize=8)

# axs[0, 1].plot(ls_df[1].index.to_numpy(), ls_df[1].iloc[:, 1].to_numpy())
# axs[0, 1].set(xlabel="N", ylabel="Time", title="Binary Search")
# axs[0, 1].tick_params(axis='x', labelsize=8)
# axs[0, 1].tick_params(axis='y', labelsize=8)


# axs[1, 0].plot(ls_df[2].index.to_numpy(), ls_df[2].iloc[:, 1].to_numpy())
# axs[1, 0].set(xlabel="N", ylabel="Time", title="Ternary Search Tree")
# axs[1, 0].tick_params(axis='x', labelsize=8)
# axs[1, 0].tick_params(axis='y', labelsize=8)


# axs[1, 1].plot(ls_df[3].index.to_numpy(), ls_df[3].iloc[:, 1].to_numpy())
# axs[1, 1].set(xlabel="N", ylabel="Time", title="Tree Set")
# axs[1, 1].tick_params(axis='x', labelsize=8)
# axs[1, 1].tick_params(axis='y', labelsize=8)


# fig.tight_layout()
# fig.subplots_adjust(top=0.88)
# fig.suptitle("allMatches runtime", y=.98, x=.56)
# plt.savefig("allMatches_plot.png")

