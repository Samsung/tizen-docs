using System;
using Tizen.NUI;
using Tizen.NUI.BaseComponents;
using Tizen.NUI.Components;

namespace NUIXamlSimpleApp
{
	public partial class XamlPage : ContentPage
	{
		static bool visiblity = true;
        	public XamlPage()
	        {
	            InitializeComponent();
	        }

	        private void btn_Clicked(object sender, ClickedEventArgs e)
	        {
	            if (visiblity)
	            {
	                popup.Hide();
	                btn.Text = "Show Popup!";
	            }
	            else
	            {
	                popup.Show();
	                btn.Text = "Hide Popup!";
	            }
	            visiblity = !visiblity;
	        }
	}
}
