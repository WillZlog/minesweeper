# Mine Sweeper

## Results

runs at a rate of 

```
y = -.4306474946x^2 + 2.995045752x + 88.82095861
```

where y is the expected wins and x is the density calculated by the equation:

```
x = mines/side_length**2
```
the bot usually maximizes win rate at 3% density and reaches an avg win rate of around 0 at around 20-30%.

## Time taken

the bot takes an average of 
```
0.00013 seconds
```
per call 