

# Maximum Relative Entropy (MrE) Model

This project demonstrates the application of the **Maximum Relative Entropy (MrE)** method for updating probability distributions using both observed data and moment constraints.

## Project Structure

```
.
├── main.py
├── mre_model.py
├── data
│   └── sample_data.csv
└── results
    └── posterior_distribution.csv
```

## Prerequisites

- Python 3.x
- Install required libraries:

```bash
pip install pandas numpy scipy
```

## Running the Project

1. **Prepare your data**: Ensure `data/sample_data.csv` contains your sample data with columns representing different categories.
2. **Set expected average**: Modify the `expected_average` variable in `main.py` as needed.
3. **Run the script**:

```bash
python main.py
```

4. **View Results**: The posterior distribution will be displayed in the console and saved in `results/posterior_distribution.csv`.

## Sample Data Format (`data/sample_data.csv`)

```
Type1,Type2,Type3
11,2,7
```

## Output Example

```
Posterior Distribution:
    Type  Probability
0  Type1     0.2942
1  Type2     0.1115
2  Type3     0.5942

Results saved to 'results/posterior_distribution.csv'
```

## License

MIT License

---

Let me know if you'd like any changes or additional features! 🚀
