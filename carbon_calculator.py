{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "1ec53bec-20b4-4b66-9c2f-bbed4549aeb4",
   "metadata": {},
   "outputs": [],
   "source": [
    "def calculate_carbon_sequestration(tree_count, avg_carbon_per_tree):\n",
    "    \"\"\"\n",
    "    Calculate total carbon sequestration in a forest.\n",
    "    Args:\n",
    "        tree_count (int): Number of trees in the forest\n",
    "        avg_carbon_per_tree (float): Average carbon sequestered per tree (in kg)\n",
    "    Returns:\n",
    "        float: Total carbon sequestered (in tonnes)\n",
    "    \"\"\"\n",
    "    total_carbon = (tree_count * avg_carbon_per_tree) / 1000  # convert to tonnes\n",
    "    return total_carbon"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "0c63f13e-f6f1-48de-946e-34fe88dd8af0",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "111.5\n"
     ]
    }
   ],
   "source": [
    "print(calculate_carbon_sequestration(5000, 22.3))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "39d16d4b-1eaf-4139-86ca-d6d2e840a388",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
