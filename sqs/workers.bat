for /l %%A in (1,1,4) do (
    start cmd /c "py worker.py"
)