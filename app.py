import streamlit as st
import pandas as pd
from backend.package_fetcher import get_installed_packages
from backend.size_calculator import get_package_size
from backend.uninstaller import uninstall_package

# Title and header
st.set_page_config(page_title="Pip Package Visualizer", layout="wide")
st.title("📦 Pip Package Visualizer")

# Fetch installed packages
with st.spinner("Fetching installed packages..."):
    packages = get_installed_packages()

# Calculate sizes (this could be slow; in a real app you'd cache this)
data = []
for pkg in packages:
    size = get_package_size(pkg['name'])
    if size:
        data.append({
            'name': pkg['name'],
            'version': pkg['version'],
            'size_bytes': size,
            'size_mb': round(size / (1024 * 1024), 2)
        })

# Convert to DataFrame
df = pd.DataFrame(data)
df = df.sort_values(by="size_mb", ascending=False)

# Layout: chart and table side-by-side
col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("📊 Package Size Distribution")
    if not df.empty:
        st.plotly_chart({
            "data": [{
                "labels": df["name"],
                "values": df["size_mb"],
                "type": "pie",
                "hole": 0.4,
                "textinfo": "label+percent"
            }],
            "layout": {
                "margin": {"t": 20, "b": 0, "l": 0, "r": 0}
            }
        }, use_container_width=True)
    else:
        st.info("No package size data available.")

with col2:
    st.subheader("🔍 Uninstall a Package")
    package_names = df["name"].tolist()
    selected_pkg = st.selectbox("Select a package", options=package_names)

    if st.button(f"Uninstall '{selected_pkg}'"):
        with st.spinner(f"Uninstalling {selected_pkg}..."):
            success = uninstall_package(selected_pkg)
            if success:
                st.success(f"✅ {selected_pkg} was uninstalled successfully.")
                st.rerun()
            else:
                st.error(f"❌ Failed to uninstall {selected_pkg}.")

# Optional: show full table below
st.markdown("---")
st.subheader("📋 Installed Packages Table")
st.dataframe(df[["name", "version", "size_mb"]].rename(columns={"size_mb": "Size (MB)"}))
