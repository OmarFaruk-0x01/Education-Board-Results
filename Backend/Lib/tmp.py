
# def GenarateHtml(dataObj):
#     tmp = ""
#     for row in dataObj['subject_grades']:
#         tmp += f"""
#         <tr>
#                <td align="left" bgcolor="#DEE1E4" valign="middle">
#                 {row['subjectCode']}
#                </td>
#                <td align="left" bgcolor="#DEE1E4" valign="middle">
#                 {row['subjectName']}
#                </td>
#                <td align="left" bgcolor="#DEE1E4" valign="middle">
#                 {row['subjectGPA']}
#                </td>
#               </tr>
#         """

#     return f"""
# <body>
#  <table align="center" border="0" cellpadding="0" cellspacing="0" width="650">
#   <tr>
#    <td>
#     <table align="center" bgcolor="#FFFFFF" border="0" cellpadding="0" cellspacing="0" width="650">
#      <tr>
#       <td align="left" background="http://www.educationboardresults.gov.bd/images/back_cor_left_top.gif" valign="top" width="12">
#        <img height="12" src="http://www.educationboardresults.gov.bd/images/trans.gif" width="12"/>
#       </td>
#       <td background="http://www.educationboardresults.gov.bd/images/back_top.gif" valign="top">
#        <img height="12" src="http://www.educationboardresults.gov.bd/images/trans.gif" width="12"/>
#       </td>
#       <td align="right" background="http://www.educationboardresults.gov.bd/images/back_cor_right_top.gif" valign="top" width="12">
#        <img height="12" src="http://www.educationboardresults.gov.bd/images/trans.gif" width="12"/>
#       </td>
#      </tr>
#      <tr>
#       <td align="left" background="http://www.educationboardresults.gov.bd/images/back_left.gif" valign="top">
#       </td>
#       <td valign="top">
#        <table border="0" cellpadding="0" cellspacing="0" width="100%">
#         <tr>
#          <td align="center" bgcolor="#EEEEEE" class="left_round" height="121" valign="middle" width="142">
#           <img height="82" src="http://www.educationboardresults.gov.bd/images/bd_logo.png" width="82"/>
#          </td>
#          <td width="2">
#           <img height="1" src="http://www.educationboardresults.gov.bd/images/trans.gif" width="2"/>
#          </td>
#          <td bgcolor="#007814" valign="top">
#           <table border="0" cellpadding="0" cellspacing="0" width="100%">
#            <tr>
#             <td align="right">
#              <table border="0" cellpadding="0" cellspacing="0" width="100%">
#               <tr>
#                <td align="left" valign="bottom">
#                 <h1 id="site_title_des">
#                  Ministry of Education
#                 </h1>
#                </td>
#                <td align="right" valign="top">
#                 <img border="0" height="41" hspace="0" src="http://www.educationboardresults.gov.bd/images/banner_flag.jpg" vspace="0" width="220"/>
#                </td>
#               </tr>
#              </table>
#             </td>
#            </tr>
#            <tr>
#             <td align="left" bgcolor="#479e55">
#              <img height="1" src="http://www.educationboardresults.gov.bd/images/trans.gif" width="1"/>
#             </td>
#            </tr>
#            <tr>
#             <td align="left" height="55">
#              <h1 id="site_title">
#               Intermediate and Secondary Education Boards Bangladesh
#              </h1>
#             </td>
#            </tr>
#            <tr>
#             <td align="right">
#              <table border="0" cellpadding="0" cellspacing="0" width="100%">
#              </table>
#             </td>
#            </tr>
#            <tr>
#             <td align="right" bgcolor="#FFFFFF">
#              <img height="1" src="http://www.educationboardresults.gov.bd/images/trans.gif" width="1"/>
#             </td>
#            </tr>
#            <tr>
#             <td align="right" bgcolor="#86C775" class="bar_bk" height="23">
#              <a class="links02" href="http://www.educationboardresults.gov.bd/http://www.educationboard.gov.bd">
#               Official Website of Education Board
#              </a>
#             </td>
#            </tr>
#           </table>
#          </td>
#         </tr>
#        </table>
#        <img height="1" src="http://www.educationboardresults.gov.bd/images/trans.gif" width="1"/>
#       </td>
#       <td align="right" background="http://www.educationboardresults.gov.bd/images/back_right.gif" valign="top">
#       </td>
#      </tr>
#     </table>
#    </td>
#   </tr>
#   <tr>
#    <td>
#     <table align="center" bgcolor="#FFFFFF" border="0" cellpadding="0" cellspacing="0" width="650">
#      <tr>
#       <td align="left" background="http://www.educationboardresults.gov.bd/images/back_left.gif" valign="top" width="12">
#       </td>
#       <td valign="top">
#        <table border="0" cellpadding="0" cellspacing="0" width="100%">
#         <tr>
#          <td align="center" class="black16bold" height="50" valign="middle">
#           SSC/Dakhil/Equivalent Result 2020
#          </td>
#         </tr>
#         <tr>
#          <td align="center" valign="middle">
#           <table border="0" cellpadding="0" cellspacing="0" width="100%">
#            <tr>
#             <td align="center" valign="middle">
#              <table border="0" cellpadding="3" cellspacing="1" class="black12" width="100%">
#               <tr>
#                <td align="left" bgcolor="#EEEEEE" valign="middle" width="12%">
#                 Roll No
#                </td>
#                <td align="left" bgcolor="#EEEEEE" valign="middle" width="27%">
#                 {dataObj['roll']}
#                </td>
#                <td align="left" bgcolor="#EEEEEE" valign="middle" width="22%">
#                 Name
#                </td>
#                <td align="left" bgcolor="#EEEEEE" valign="middle" width="39%">
#                 {dataObj['name']}
#                </td>
#               </tr>
#               <tr>
#                <td align="left" bgcolor="#EEEEEE" valign="middle">
#                 Board
#                </td>
#                <td align="left" bgcolor="#EEEEEE" valign="middle">
#                 {dataObj['board']}
#                </td>
#                <td align="left" bgcolor="#EEEEEE" valign="middle">
#                 Father's Name
#                </td>
#                <td align="left" bgcolor="#EEEEEE" valign="middle">
#                 {dataObj['father_name']}
#                </td>
#               </tr>
#               <tr>
#                <td align="left" bgcolor="#EEEEEE" valign="middle">
#                 Group
#                </td>
#                <td align="left" bgcolor="#EEEEEE" valign="middle">
#                 {dataObj['group']}
#                </td>
#                <td align="left" bgcolor="#EEEEEE" valign="middle">
#                 Mother's Name
#                </td>
#                <td align="left" bgcolor="#EEEEEE" valign="middle">
#                 {dataObj['mother_name']}
#                </td>
#               </tr>
#               <tr>
#                <td align="left" bgcolor="#EEEEEE" valign="middle">
#                 Type
#                </td>
#                <td align="left" bgcolor="#EEEEEE" valign="middle">
#                 {dataObj['type']}
#                </td>
#                <td align="left" bgcolor="#EEEEEE" valign="middle">
#                 Date of Birth
#                </td>
#                <td align="left" bgcolor="#EEEEEE" valign="middle">
#                 {dataObj['dob']}
#                </td>
#               </tr>
#               <tr>
#                <td align="left" bgcolor="#EEEEEE" valign="middle">
#                 Result
#                </td>
#                <td align="left" bgcolor="#EEEEEE" class="black12bold" valign="middle">
#                 {dataObj['result']}
#                </td>
#                <td align="left" bgcolor="#EEEEEE" valign="middle">
#                 Institute
#                </td>
#                <td align="left" bgcolor="#EEEEEE" valign="middle">
#                 {dataObj['institute']}
#                </td>
#               </tr>
#               <tr>
#                <td align="left" bgcolor="#EEEEEE" valign="middle">
#                 GPA
#                </td>
#                <td align="left" bgcolor="#EEEEEE" class="black12bold" colspan="3" valign="middle">
#                 {dataObj['gpa']}
#                </td>
#               </tr>
#              </table>
#             </td>
#            </tr>
#            <tr>
#             <td align="center" height="40" valign="middle">
#              <span class="black16bold">
#               Grade Sheet
#              </span>
#             </td>
#            </tr>
#            <tr>
#             <td align="center" valign="middle">
#              <table border="0" cellpadding="3" cellspacing="1" class="black12" width="100%">
#               <tr class="black12bold">
#                <td align="left" bgcolor="#AFB7BE" valign="middle" width="19%">
#                 Code
#                </td>
#                <td align="left" bgcolor="#AFB7BE" valign="middle" width="66%">
#                 Subject
#                </td>
#                <td align="left" bgcolor="#AFB7BE" valign="middle" width="15%">
#                 Grade
#                </td>
#               </tr>

#               {tmp}
#              </table>
#             </td>
#            </tr>
#           </table>
#          </td>
#         </tr>
#         <tr>
#          <td align="center" height="40" valign="middle">
#           <a class="links" href="http://www.educationboardresults.gov.bd/index.php">
#            Search Again
#           </a>
#          </td>
#         </tr>
#         <tr>
#          <td>
#           <table border="0" cellpadding="0" cellspacing="0" width="626">
#            <tr bgcolor="#86c775">
#             <td colspan="5">
#              <img height="5" src="http://www.educationboardresults.gov.bd/images/trans.gif" width="1"/>
#             </td>
#            </tr>
#            <tr>
#             <td colspan="5">
#              <img height="1" src="http://www.educationboardresults.gov.bd/images/trans.gif" width="1"/>
#             </td>
#            </tr>
#            <tr>
#             <td align="left" bgcolor="#F2F2F2" class="footer_text" valign="bottom" width="5">
#              <img height="5" src="http://www.educationboardresults.gov.bd/images/footer_corner_left.gif" width="5"/>
#             </td>
#             <td align="left" bgcolor="#F2F2F2" class="footer_text" height="70" valign="middle" width="356">
#              �2005-2020  Ministry of Education, All rights reserved.
#             </td>
#             <td align="right" bgcolor="#F2F2F2" class="footer_text" height="70" valign="middle" width="150">
#              Powered by
#              <img height="5" src="http://www.educationboardresults.gov.bd/images/footer_corner_right.gif" width="5"/>
#             </td>
#             <td align="center" bgcolor="#F2F2F2" height="70" valign="middle" width="110">
#              <img height="44" src="http://www.educationboardresults.gov.bd/images/tbl_logo.png" width="83"/>
#             </td>
#             <td align="left" bgcolor="#F2F2F2" class="footer_text" valign="bottom" width="5">
#              <img height="5" src="http://www.educationboardresults.gov.bd/images/footer_corner_right.gif" width="5"/>
#             </td>
#            </tr>
#           </table>
#          </td>
#         </tr>
#        </table>
#       </td>
#       <td align="right" background="http://www.educationboardresults.gov.bd/images/back_right.gif" valign="top" width="12">
#       </td>
#      </tr>
#      <tr>
#       <td align="left" background="http://www.educationboardresults.gov.bd/images/back_cor_left_bot.gif" valign="top">
#        <img height="12" src="http://www.educationboardresults.gov.bd/images/trans.gif" width="12"/>
#       </td>
#       <td background="http://www.educationboardresults.gov.bd/images/back_bot.gif" valign="top">
#        <img height="12" src="http://www.educationboardresults.gov.bd/images/trans.gif" width="12"/>
#       </td>
#       <td align="right" background="http://www.educationboardresults.gov.bd/images/back_cor_right_bot.gif" valign="top">
#        <img height="12" src="http://www.educationboardresults.gov.bd/images/trans.gif" width="12"/>
#       </td>
#      </tr>
#     </table>
#    </td>
#   </tr>
#   <tr>
#    <td>
#    </td>
#   </tr>
#  </table>
# </body>
#     """
