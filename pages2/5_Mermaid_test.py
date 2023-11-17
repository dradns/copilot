import os
import streamlit as st
from components.sidebar import sidebar
#import streamlit_mermaid as stmd
from functions.stmd import st_mermaid

#TITLES
st.set_page_config(page_title="Analyst copilot", page_icon="📖", layout="wide")

# Enable caching for expensive functions
#bootstrap_caching()

sidebar()

code = """
sequenceDiagram
    User->>ApiGw: Upload Document Request
    ApiGw->>MicroService: Forward Document
    MicroService->>ObjectDb: Store Document
    ObjectDb-->>MicroService: Document ID
    MicroService->>RelationalDb: Store Document Metadata
    RelationalDb-->>MicroService: Acknowledge Metadata Storage
    MicroService->>ApiGw: Respond with Document ID
    ApiGw->>User: Document ID

"""

# code = """
#     graph LR
#     A[Start] --> B(Mermaid World) --> C(Underwater City) --> D(Mermaid's Home)
# """

code2 = """
    C4Context
      title System Context diagram for Internet Banking System
      Enterprise_Boundary(b0, "BankBoundary0") {
        Person(customerA, "Banking Customer A", "A customer of the bank, with personal bank accounts.")
        Person(customerB, "Banking Customer B")
        Person_Ext(customerC, "Banking Customer C", "desc")

        Person(customerD, "Banking Customer D", "A customer of the bank, <br/> with personal bank accounts.")

        System(SystemAA, "Internet Banking System", "Allows customers to view information about their bank accounts, and make payments.")

        Enterprise_Boundary(b1, "BankBoundary") {

          SystemDb_Ext(SystemE, "Mainframe Banking System", "Stores all of the core banking information about customers, accounts, transactions, etc.")

          System_Boundary(b2, "BankBoundary2") {
            System(SystemA, "Banking System A")
            System(SystemB, "Banking System B", "A system of the bank, with personal bank accounts. next line.")
          }

          System_Ext(SystemC, "E-mail system", "The internal Microsoft Exchange e-mail system.")
          SystemDb(SystemD, "Banking System D Database", "A system of the bank, with personal bank accounts.")

          Boundary(b3, "BankBoundary3", "boundary") {
            SystemQueue(SystemF, "Banking System F Queue", "A system of the bank.")
            SystemQueue_Ext(SystemG, "Banking System G Queue", "A system of the bank, with personal bank accounts.")
          }
        }
      }

      BiRel(customerA, SystemAA, "Uses")
      BiRel(SystemAA, SystemE, "Uses")
      Rel(SystemAA, SystemC, "Sends e-mails", "SMTP")
      Rel(SystemC, customerA, "Sends e-mails to")

      UpdateElementStyle(customerA, $fontColor="red", $bgColor="grey", $borderColor="red")
      UpdateRelStyle(customerA, SystemAA, $textColor="blue", $lineColor="blue", $offsetX="5")
      UpdateRelStyle(SystemAA, SystemE, $textColor="blue", $lineColor="blue", $offsetY="-10")
      UpdateRelStyle(SystemAA, SystemC, $textColor="blue", $lineColor="blue", $offsetY="-40", $offsetX="-50")
      UpdateRelStyle(SystemC, customerA, $textColor="red", $lineColor="red", $offsetX="-50", $offsetY="20")

      UpdateLayoutConfig($c4ShapeInRow="3", $c4BoundaryInRow="1")
"""

mermaid = st_mermaid(code, key=1, height="500px")
mermaid2 = st_mermaid(code2, key=2, height="1500px", width="700px")
#st.write(mermaid)
#st.write(code)
