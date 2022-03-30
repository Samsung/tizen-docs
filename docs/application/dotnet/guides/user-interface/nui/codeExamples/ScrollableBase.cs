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
            for (int i = 0; i <= 60; ++i)
            {
                var t = new TextLabel
                {
                    Text = String.Format("I am label #{0}", i),
                    Size2D = new Size2D(NUIApplication.GetDefaultWindow().WindowSize.Width, 70),
                };
                Scroller.Add(t);
            }

            btn.Clicked += (o, e) =>
            {
                Scroller.ScrollTo(500, true);
            };			
		}
	}
}
