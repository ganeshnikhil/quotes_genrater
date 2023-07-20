import tkinter as tk
from random import randint

root = tk.Tk()
root.title('Positive Message Generator')
root.geometry('1350x900')
root.configure(background='#20bd8e', relief="solid", borderwidth=10)
# Creating a frame to act as the border
#3B3C36  Black olive
#36454F  charcoal 
#232B2B  Charleston green
#010127  Black Rock
#333333  Dark Charcoal
#060D0D  Luxury Black
#004242  Warm Black
border_frame = tk.Frame(root, bg= '#004242', relief="groove", bd=10)
border_frame.pack(fill='both', expand=True)
#Dim gray 
# Writing Label for heading
heading_label = tk.Label(
    border_frame,
    text="Positive Message Generator",
    font="Courier 40 bold",
    anchor='center',
    bg='#20bd8e',
    fg="black",
    relief="solid",
    bd=10
)
heading_label.pack(pady=60)


# Creating a list of quotes
quotes_list = [
    "1. You've taken the first step towards overcoming alcoholism. It's a courageous decision!",
    "2. Every small victory over alcoholism brings you closer to a healthier and happier life.",
    "3. Your commitment to your recovery journey is commendable. Keep going!",
    "4. Remember, you are not defined by your past struggles. Your future is bright and full of possibilities.",
    "5. Surround yourself with a supportive network that understands and encourages your sobriety.",
    "6. Celebrate your progress, no matter how small. Each day without alcohol is a milestone worth acknowledging!",
    "7. Your determination to break free from the grip of alcoholism is truly inspiring to others around you.",
    "8. Focus on self-care and prioritize your physical and mental well-being. You deserve it!",
    "9. Embrace a positive mindset and believe in your ability to overcome any challenges that come your way.",
    "10. Your resilience and strength in the face of alcoholism make you a true warrior. Keep fighting!",
    "11. Your decision to prioritize your health and well-being by overcoming alcoholism is a testament to your inner strength.",
    "12. Each day you abstain from alcohol, you are reclaiming control of your life and creating a brighter future.",
    "13. Remember, setbacks are a natural part of the recovery journey. Learn from them and keep moving forward.",
    "14. Your sobriety is a powerful inspiration to those who may be struggling. You have the potential to make a positive impact.",
    "15. Believe in yourself and your ability to overcome alcoholism. You are stronger than you realize.",
    "16. Seek support from others who have walked a similar path. Together, you can find strength and encouragement.",
    "17. Take pride in your sobriety journey. It takes courage and determination to choose a healthier lifestyle.",
    "18. Celebrate the small victories along the way. They are signs of progress and a testament to your commitment.",
    "19. Remember, you are not alone in this. Reach out to others for support and guidance when you need it.",
    "20. Your decision to prioritize self-care and sobriety will lead to a happier, more fulfilling life.",
    "21. Embrace the positive changes that sobriety brings. You are rewriting your story and creating a brighter future.",
    "22. Focus on the present moment and the choices that will lead you to a healthier, alcohol-free life.",
    "23. Surround yourself with people who believe in your ability to overcome alcoholism. Their support is invaluable.",
    "24. Remind yourself of the reasons why you chose sobriety. They will fuel your determination during challenging times.",
    "25. Your resilience and determination in the face of alcoholism are qualities to be proud of. Keep pushing forward!",
    "26. Embrace a growth mindset. View challenges as opportunities for personal growth and transformation.",
    "27. Your journey to recovery is unique, and it's okay to progress at your own pace. Trust the process.",
    "28. Stay committed to self-improvement and personal development. You have the power to shape a brighter future.",
    "29. Reflect on how far you've come on your sobriety journey. Your progress is a testament to your strength and resilience.",
    "30. Each day without alcohol is an opportunity for personal growth and a step towards a more fulfilling life.",
    "31. Celebrate your sobriety milestones and the positive impact they have on your physical and mental well-being.",
    "32. Trust in your ability to overcome any obstacles that come your way. You have the strength within you.",
    "33. Embrace the joy and freedom that comes with a life free from the grip of alcoholism.",
    "34. You are rewriting your story and creating a legacy of resilience and triumph over alcoholism.",
    "35. Your sobriety journey is an act of self-love and self-respect. You deserve a life filled with happiness and fulfillment.",
    "36. Recognize the progress you've made on your sobriety journey. You are making positive changes every day.",
    "37. Your decision to face alcoholism head-on shows immense bravery and a commitment to personal growth.",
    "38. Believe in the power of second chances. You have the opportunity to create a new, alcohol-free chapter in your life.",
    "39. Embrace the challenges that come with sobriety. They are opportunities for personal growth and transformation.",
    "40. Your sobriety journey is a testament to your resilience and unwavering determination. Keep going!",
    "41. Celebrate your uniqueness and the strength it takes to carve your own path to sobriety.",
    "42. Your decision to prioritize sobriety is an investment in your physical, emotional, and mental well-being.",
    "43. Surround yourself with positive influences and uplifting environments that support your alcohol-free lifestyle.",
    "44. Remind yourself of the freedom and clarity that sobriety brings. It's a gift worth cherishing.",
    "45. Your commitment to sobriety inspires hope in others who may be struggling. You are a beacon of light.",
    "46. Each day without alcohol is an opportunity to rediscover yourself and build a life that aligns with your values.",
    "47. Celebrate your resilience in overcoming alcoholism. You have the strength to conquer any challenge.",
    "48. View setbacks as learning opportunities rather than failures. They provide valuable insights for growth.",
    "49. Your journey to sobriety is a testament to your willingness to embrace change and pursue a better future.",
    "50. Focus on the progress you've made rather than dwelling on past mistakes. You are evolving and growing.",
    "51. Embrace gratitude for the small blessings in your life. Sobriety opens your eyes to the beauty around you.",
    "52. Trust in the process of recovery. It may have its ups and downs, but it leads to a life filled with possibility.",
    "53. Your sobriety journey is an act of self-empowerment. You are taking control of your life and shaping your destiny.",
    "54. Seek inspiration from others who have successfully overcome alcoholism. Their stories are proof that recovery is possible.",
    "55. Embrace self-forgiveness and let go of any guilt or shame associated with past experiences. You deserve healing.",
    "56. Remember, you are not defined by your past. Your future is bright and full of endless opportunities.",
    "57. Surround yourself with love and support. Healthy relationships nurture your sobriety and foster personal growth.",
    "58. Your journey to sobriety is a gift you give to yourself and those who care about you. You are making a positive impact.",
    "59. Embrace self-compassion. Treat yourself with kindness and understanding as you navigate the challenges of recovery.",
    "60. Celebrate the milestones of your sobriety journey.Each one represents progress and a triumph over alcoholism."]


# Initializing label_text with a default value
label_text = None

# Function to display random quotes
def random_quote_function():
    global label_text
    if label_text:
        label_text.destroy()
    length_list = len(quotes_list)
    random_quote = randint(0, length_list - 1)
    msg = quotes_list[random_quote].replace(".", "\n").replace(',',"\n")
    label_text = tk.Label(
        border_frame,
        text=msg,
        font=("Verdana", 19, "bold italic"),
        bg='#20bd8e',
        fg='white',
        relief="solid",
        bd=7
    )
    label_text.pack(pady=100)
    label_text.bind("<Enter>", on_enter)
    label_text.bind("<Leave>", on_leave)

def on_enter(event):
    label_text.config(foreground="red", cursor="ibeam")

def on_leave(event):
    label_text.config(foreground="black", cursor="arrow")

# Button to display quotes randomly
display_button = tk.Button(
    border_frame,
    text="Quotes",
    relief="raised",
    font=("Courier", 20, "bold"),
    bg='orange',
    fg='green',
    command=random_quote_function,
    anchor=tk.CENTER
)
display_button.configure(
    activebackground="red",
    activeforeground="yellow"
)
display_button.pack()

# Quit button
quit_button = tk.Button(
    border_frame,
    text="Quit",
    relief="raised",
    font=("Courier", 20, "bold"),
    bg='orange',
    fg='red',
    command=root.destroy,
    anchor=tk.CENTER
)
quit_button.pack(pady=30)
root.mainloop()
