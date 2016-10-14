import clr
clr.AddReference("System")
import System
import System.Diagnostics

def stopWatchTest():
	stopWatch = System.Diagnostics.Stopwatch()
	stopWatch.Start()
	print "This takes place during the timing period."
	stopWatch.Stop()
	print stopWatch.ElapsedMilliseconds.ToString() + " milliseconds to perform the previous operation."
	print stopWatch.Elapsed.ToString() + " total time elapsed."

stopWatchTest()