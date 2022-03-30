using System;
using Tizen.NUI;
using Tizen.NUI.BaseComponents;
using Tizen.NUI.Components;

namespace NUIXamlSimpleApp
{
	public partial class XamlPage : ContentPage
	{
		private DateTime date;
		private DatePicker datePicker;
		public XamlPage()
		{
			InitializeComponent();
			date = DateTime.Now;
			picker.Time=time;
		}
	}
}
