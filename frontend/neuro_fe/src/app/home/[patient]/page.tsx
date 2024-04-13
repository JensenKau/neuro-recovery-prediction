import React from "react";
import HomeIcon from "../../components/HomeIcon";
import MyItems from "../../components/MyItems";
import EditIcon from "@mui/icons-material/Edit";
import CustomButton from "../../components/CustomButton";
import PatientForm from "../../components/PatientForm";
import ShareIcon from "@mui/icons-material/Share";
import ShareForm from "../../components/ShareProfile";

const page = ({ params }: any) => {
  const patientName = decodeURIComponent(params.patient);
  return (
    <div className="mt-[50px] mb-[40px] ml-[50px] mr-[50px]">
      <div className="flex justify-between mb-[50px]">
        <div className="flex">
          <HomeIcon />
          <div className="mt-6 ml-5 text-5xl">
            My Patients {">"}{" "}
            <span className="text-blue-600">{patientName}</span>
          </div>
        </div>
        <div className="mt-[30px]">
          <ShareForm
            title="Share Profile"
            ButtonComponent={CustomButton}
            buttonProps={{
              children: "share profile",
              icon: ShareIcon,
              style: "text",
            }}
            submitFormInfo="done"
          />
        </div>
      </div>
      <MyItems
        initialItems={[
          "First Name: ",
          "Last Name: ",
          "Age: ",
          "Gender: ",
          "ROSC: ",
          "OHCA: ",
          "Shockable Rhythm: ",
          "TTM: ",
        ]}
        childrenSize="3xl"
        FormButtonComponent={PatientForm}
        FormButtonProps={{
          title: "Edit Patient Infomation",
          ButtonComponent: CustomButton,
          buttonProps: { children: "Edit", icon: EditIcon, style: "outlined" },
          submitFormInfo: "save changes",
        }}
        chipsHeight="55px"
        chipsWidth="327px"
        chipsClickable={false}
        chipsLinkable={false}
      >
        Pateint Information
      </MyItems>
    </div>
  );
};

export default page;
