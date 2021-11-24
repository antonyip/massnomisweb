
import streamlit as st



from multiapp import MultiApp

from apps import MIDNOVLUNA,midnovSUSHI,THORCHAINMIDNOV,testt,levanaspecial,MINELUNA,earlynovTHOR,minestaking,defilamatry1,aave29,beth,FlipsideValidator,flashy,aaavemidoctoberbatch,thorchain,aave_migration,bluna,compare,eth_fees,eth_matic_vol,extra,GPdata,gpusers,home,loop1,loop2,polygon_fees,steth


# import your app modules here
app = MultiApp()

st.set_page_config(layout="wide")
page = st.container()
st.markdown("""
# 
""")
st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)
st.markdown("""
<nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #3498DB;">
  <a class="navbar-brand" href="https://app.ens.domains/name/massnomis.eth/details" target="_blank">massnomis</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav">
      <li class="nav-item active">
        <a class="nav-link disabled" href="#">Home <span class="sr-only">(current)</span></a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="https://github.com/massnomis/massnomisweb" target="_blank">GitHub</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="https://twitter.com/sammycrypto4" target="_blank">Twitter</a>
      </li>
    </ul>
  </div>
</nav>
""", unsafe_allow_html=True)

# Add all your application here
app.add_app("HOME", home.app)
app.add_app("AAVE:29", aave29.app)
app.add_app("eth_fees:?", eth_fees.app)
#...

app.run()