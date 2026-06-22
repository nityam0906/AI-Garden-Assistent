import streamlit as st

st.title("🌱 AI Garden Assistant")

plant = st.text_input("Plant Name")
problem = st.text_area("Describe the plant problem")

if st.button("Analyze"):
    st.success("Analysis Complete")
    st.write("Plant:", plant)
    st.write("Problem:", problem)

    st.write("### Recommendations")

if "yellow" in problem.lower():
    st.write("- Possible nitrogen deficiency")
    st.write("- Add vermicompost or cow manure")
elif "dry" in problem.lower():
    st.write("- Increase watering frequency")
    st.write("- Mulch the soil")
else:
    st.write("- Monitor plant health regularly")