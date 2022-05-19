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
            slider1.ValueChanged += (o, e) =>
            {
                text1.Text = "slider value: " + slider1.CurrentValue;
            };
		}
	}
}
