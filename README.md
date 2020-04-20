# Garbage Math for Python

    from garbage import Garbage

    precise_number = 42

    assert precise_number + Garbage == Garbage
    assert precise_number * Garbage == Garbage
    assert sqrt(Garbage) == Garbage
    assert Garbage**2 == Garbage
    assert precise_number**Garbage == Garbage
    assert Garbage - Garbage == Garbage
    assert precise_number / (Garbage - Garbage) == Garbage
    assert Garbage * 0 == 0
    
---

!['Garbage In, Garbage Out' should not be taken to imply any sort of conservation law limiting the amount of garbage produced.](https://imgs.xkcd.com/comics/garbage_math.png)

[https://xkcd.com/2295/]
