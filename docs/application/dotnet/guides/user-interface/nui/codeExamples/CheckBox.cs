using System;
using Tizen.NUI;
using Tizen.NUI.BaseComponents;
using Tizen.NUI.Components;

namespace NUIXamlSimpleApp
{
	public partial class XamlPage : ContentPage
	{
		public XamlPage()
		{	
			InitializeComponent();
			checkBox1.Clicked += (o, e) =>
			{
				if (checkBox1.IsSelected)
				{
					checkBox1.Text = "True";
				}
				else
				{
					checkBox1.Text = "False";
				}
			};
		}
	}
}
