import os
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.utils import ImageReader

# Phase Diagrams Data
def pb_sn_phase_diagram():
    return "Pb-Sn Phase Diagram"

def fe_c_phase_diagram():
    return "Fe-C Phase Diagram"

def cu_ni_phase_diagram():
    return "Cu-Ni Phase Diagram"

# Lever Rule Calculation
def lever_rule(overall_composition, phase_a_comp, phase_b_comp):
    if phase_a_comp == phase_b_comp:
        raise ValueError("Phase compositions cannot be identical.")
    fraction_b = (overall_composition - phase_a_comp) / (phase_b_comp - phase_a_comp)
    fraction_a = 1 - fraction_b
    return fraction_a, fraction_b

# PDF
def save_to_pdf(diagram_name, overall_comp, temp, phase_a_comp, phase_b_comp, fraction_a, fraction_b, image_path,
                save_path):

    pdf_filename = f"{overall_comp:.2f}_at_{temp:.0f}C_{diagram_name.replace(' ', '_')}.pdf"
    pdf_path = os.path.join(save_path, pdf_filename)
    pdf = canvas.Canvas(pdf_path, pagesize=letter)
    pdf.setTitle("Phase Diagram Report")

    # Header
    pdf.setFont("Helvetica-Bold", 16)
    pdf.drawString(100, 750, "Phase Diagram Report")
    pdf.setFont("Helvetica", 12)

    # Add Diagram Info
    pdf.drawString(100, 700, f"Selected Phase Diagram: {diagram_name}")
    pdf.drawString(100, 680, f"Overall Composition: {overall_comp:.2f} wt%")
    pdf.drawString(100, 660, f"Temperature: {temp:.2f} °C")
    pdf.drawString(100, 640, f"Phase A Composition: {phase_a_comp:.2f} wt%")
    pdf.drawString(100, 620, f"Phase B Composition: {phase_b_comp:.2f} wt%")
    pdf.drawString(100, 600, f"Fraction of Phase A: {fraction_a:.2f}")
    pdf.drawString(100, 580, f"Fraction of Phase B: {fraction_b:.2f}")


    if os.path.exists(image_path):
        pdf.drawImage(ImageReader(image_path), 100, 280, width=400, height=300)
    else:
        pdf.drawString(100, 560, "Image file not found. No diagram included.")

    pdf.setFont("Helvetica-Oblique", 10)
    pdf.drawString(100, 210, "Lever Rule and Tie-Line methods applied for calculations.")
    pdf.save()
    print(f"PDF report generated: {pdf_path}")


# Main Program
def main():
    print("Welcome to Alloy Phase Diagram Calculator")
    print("Select the Phase Diagram:")
    print("1. Pb-Sn")
    print("2. Fe-C")
    print("3. Cu-Ni")
    choice = input("Enter your choice (1-3): ")

    # Phase diagram and its diagram
    if choice == "1":
        diagram_name = pb_sn_phase_diagram()
        image_path = r"C:\Users\laksh\Desktop\Python PDF\program requirments\Pb-Sn-Phase-Diagram.png"
    elif choice == "2":
        diagram_name = fe_c_phase_diagram()
        image_path = r"C:\Users\laksh\Desktop\Python PDF\program requirments\Screenshot 2024-12-28 163459.png"
    elif choice == "3":
        diagram_name = cu_ni_phase_diagram()
        image_path = r"C:\Users\laksh\Desktop\Python PDF\program requirments\Screenshot 2024-12-28 162934.png"
    else:
        print("Invalid choice! Exiting program.")
        return

    overall_comp = float(input("Enter the overall composition (wt%): "))
    temp = float(input("Enter the temperature (°C): "))
    if choice == "1":
        if 50 <= temp <= 182:
            phase_a_comp = 18.3
            phase_b_comp = 97.5
        elif 183 <= temp <= 232:
            phase_a_comp = 16.0
            phase_b_comp = 60.0
        elif 233 <= temp <= 327:
            phase_a_comp = 11.0
            phase_b_comp = 51.0
        else:
            print("Temperature is outside the defined range for this phase diagram.")
            return
    if choice == "2":
        if 400 <= temp <= 727:
            phase_a_comp = 0.022
            phase_b_comp = 6.67
        elif 728 <= temp <= 1493:
            phase_a_comp = 0
            phase_b_comp = 2.11
        elif 1494 <= temp <= 1538:
            phase_a_comp = 0.1
            phase_b_comp = 0.5
        else:
            print("Temperature is outside the defined range for this phase diagram.")
            return
    if choice == "3":
        if 1000<= temp <= 1085:
            phase_a_comp = 0
            phase_b_comp = 100
        elif 1086 <= temp <= 1453:
            phase_a_comp = 28
            phase_b_comp = 72
        elif 1454 <= temp <= 1600:
            phase_a_comp = 0
            phase_b_comp = 100
        else:
            print("Temperature is outside the defined range for this phase diagram.")
            return

    try:
        fraction_a, fraction_b = lever_rule(overall_comp, phase_a_comp, phase_b_comp)
        print(f"Phase A Composition: {phase_a_comp:.2f} wt%")
        print(f"Phase B Composition: {phase_b_comp:.2f} wt%")
        print(f"Fraction of Phase A: {fraction_a:.2f}")
        print(f"Fraction of Phase B: {fraction_b:.2f}")
    except ValueError as e:
        print(f"Error in Lever Rule Calculation: {e}")
        return

    # Directory
    save_path = "C:/Users/laksh/Desktop/Python PDF"
    os.makedirs(save_path, exist_ok=True)

    # Save PDF
    save_to_pdf(diagram_name, overall_comp, temp, phase_a_comp, phase_b_comp, fraction_a, fraction_b, image_path,
                save_path)

if __name__ == "__main__":
    main()

print("Thanku For using AlloyPhaseCalucation")
print("_____________________________________")