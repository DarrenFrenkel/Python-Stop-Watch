
import simpleguitk as simplegui
# define global variables
t = 0
x = 0
y = 0
timer_running = False

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    minute = 0
    tenths_second = t % 10
    second = (t - tenths_second) % 100/10 

    subtractor = (t - tenths_second) % 100
    ten_second = (t -(tenths_second + subtractor))/100
    
    if ten_second > 5:
        minute = ten_second/6
        ten_second = ten_second % 6
	
    return str(int(minute)) + ":" + str(int(ten_second)) + str(int(second)) + "." + str(int(tenths_second))
    pass
	
	


# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    global timer_running
    timer.start()
    timer_running = True
    
    
    
def stop ():
    global x,y,timer_running
    tenths_second = t % 10
    timer.stop ()
    if timer_running == True:
        y = y+1
        if tenths_second == 0:
            x = x+1
    timer_running = False
    
    
def reset ():
    global t,x,y
    timer,stop ()
    t = 0
    x=0
    y=0
   

# define event handler for timer with 0.1 sec interval
def timer_handler():
    global t
    t = t+1
    
def numerical_counters(x,y):
   return str(x)+"/"+str(y)
        
 

# define draw handler
def draw_handler1(canvas):
    canvas.draw_text(format(t),[90,260], 60, "White")
    canvas.draw_text(numerical_counters(x,y),[310,80], 40, "Green")
    

    
    
# create frame
frame = simplegui.create_frame('Stop Watch: The Game', 400, 400)

# register event handlers
timer = simplegui.create_timer(100, timer_handler)
frame.set_draw_handler(draw_handler1)
#frame.set_draw_handler()
frame.add_button("Start", start, 80)
frame.add_button("Stop", stop, 80)
frame.add_button("Reset", reset, 80)

# start frame
frame.start()


